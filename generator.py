from textgenrnn import textgenrnn
import twitter



def getTweets():
    
    api = twitter.Api(consumer_key="{Consumer_Key}",
                      consumer_secret="{Consumer_Secret}",
                      access_token_key="{Access_Token_Key}",
                      access_token_secret="{Access_Secret}",
                      tweet_mode='extended')

    api.VerifyCredentials()

    infile = open('accounts.txt','r+')
    accounts = infile.readlines()

    for i in range(0,len(accounts)):

        accounts[i] = accounts[i].rstrip('\n')
    
    twl = []

    for account in accounts:

        tweets = api.GetUserTimeline(screen_name=account, 
                                     count=200,
                                     include_rts=False
                                    )

        for tweet in tweets:

            twl.append(tweet.full_text)

    
    return twl

def rnn():

    rnn = textgenrnn()
    rnn.train_on_texts(getTweets(),num_epochs=10)
    rnn.generate_to_file("republibot", prefix = 'Trump', 
                         n=10, 
                         temperature=[.5,.7,1], 
                         max_gen_length=280,
                         top_n=3)

def __main__():

    rnn()

__main__()


