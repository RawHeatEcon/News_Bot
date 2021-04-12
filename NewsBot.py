#Rohit_Kumar
#Newsbot_with_Trading_Algorithm
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from pynput.keyboard import Key, Controller

#CNN (Static website)
def cnn():
    print("Scanning CNN website...")
    cnn_URL = 'https://www.cnn.com/business'
    cnn_page = requests.get(cnn_URL)
    cnn_raw_code = cnn_page.content
    cnn_source = BeautifulSoup(cnn_raw_code, "html.parser")
    global cnn_headlines
    cnn_headlines = cnn_source.find_all('span', class_='cd__headline-text') 
    print("Scan complete.")
    return cnn_headlines

# Loads website, and then saves html code from news website and searches through the code to match specific 
# html chunk that returns necessary headline text only.

## Note: this is a static website that does not change code through javascript, 
# thus simplifying the scraping process.



#Forbes (Static website)
def forbes():
    print("Scanning Forbes website...")
    forbes_URL = 'https://www.forbes.com/'
    forbes_page = requests.get(forbes_URL)
    forbes_raw_code = forbes_page.content
    forbes_source = BeautifulSoup(forbes_raw_code, "html.parser")
    global forbes_headlines
    forbes_headlines = forbes_source.find_all('a', class_="happening__title")
    print("Scan complete.")
    return forbes_headlines

#Bloomberg (Dynamic website)
def bloomberg():
    print("Scanning Bloomberg website...")
    bloomberg_URL = 'https://www.bloomberg.com/markets/watchlist'
    bloomberg_page = webdriver.Firefox()
    bloomberg_page.get(bloomberg_URL)
    time.sleep(5) # wait 5 seconds for the page to load the js
    bloomberg_raw_code = bloomberg_page.execute_script("return document.documentElement.outerHTML")
    type = Controller()
    type.press(Key.alt)
    type.press(Key.space)
    type.press('c')
    type.release(Key.alt)
    type.release(Key.space)
    type.release('c') 
    #time.sleep(5)
    bloomberg_source = BeautifulSoup(bloomberg_raw_code, "html.parser")
    global bloomberg_headlines
    bloomberg_headlines = bloomberg_source.find_all('a', class_="headline__55bd5397")    
    print("Scan complete.")
    if bloomberg_headlines == ():
        print("ERROR: \n")
        print("Website html has changed, please update code")
    return bloomberg_headlines

# Similar to Static websites, begins by loading the website. 
# Since the website is dynamic, it includes bits of javascript coding that changes the underlying code,
# we pauses our scraping for a few seconds for the page to completely load, and then proceed with the same
# process of static websites.

# Make sure geckodriver executable is in the PATH that way the website can be accessed through the firefox browser
 
#MarketWatch (Dynamic website)
def marketwatch():
    print("Scanning MarketWatch website...")
    MW_URL = 'https://www.marketwatch.com/'
    MW_page = requests.get(MW_URL)
    MW_raw_code = MW_page.content
    MW_source = BeautifulSoup(MW_raw_code, "html.parser")
    global MW_headlines
    MW_headlines = MW_source.find_all('span', class_='headline')
    print("Scan complete.")
    return MW_headlines

#WallStreetJournal (Static website)
def wall_street_journal():
    print("Scanning Wall Street Journal website...")
    WSJ_URL = 'https://www.wsj.com/news/latest-headlines'
    WSJ_page = webdriver.Firefox()
    WSJ_page.get(WSJ_URL)
    time.sleep(5)
    WSJ_raw_code = WSJ_page.execute_script("return document.documentElement.outerHTML")
    type2 = Controller()
    type2.press(Key.alt)
    type2.press(Key.space)
    type2.press('c')
    type2.release(Key.alt)
    type2.release(Key.space)
    type2.release('c')
    #time.sleep(5)
    WSJ_source = BeautifulSoup(WSJ_raw_code, "html.parser")
    global WSJ_headlines
    WSJ_headlines = WSJ_source.find_all('div', class_='WSJTheme--headline--7VCzo7Ay')
    print("Scan complete.")
    if WSJ_headlines == ():
        print("ERROR: \n")
        print("Website html has changed, please update code")
    return WSJ_headlines

# The code is working as of 7/15/20, future website maintenance may cause problems within the code, and require
# debugging



def scanning():
    cnn()
    forbes()
    bloomberg()
    marketwatch()
    wall_street_journal()

#Word Lists
global positive
global negative
global very_strong
global very_weak
global neutral
global influential
positive = ["absolutely", "accepted", "acclaimed", "accomplish", "accomplishment", "achievement", "action", "active", "admire", "adorable", "adventure", "affirmative", "affluent", "agree", "agreeable", "amazing", "angelic", "appealing", "approve", "aptitude", "attractive", "awesome", "beaming", "beautiful", "believe", "beneficial", "bliss", "bountiful", "bounty", "brave", "bravo", "brilliant", "bubbly", "calm", "celebrated", "certain", "champ", "champion", "charming", "cheery", "choice", "classic", "classical", "clean", "commend", "composed", "congratulation", "constant", "cool", "courageous", "creative", "cute", "dazzling", "delight", "delightful", "distinguished", "divine", "earnest", "easy", "ecstatic", "effective", "effervescent", "efficient", "effortless", "electrifying", "elegant", "enchanting", "encouraging", "endorsed", "energetic", "energized", "engaging", "enthusiastic", "essential", "esteemed", "ethical", "excellent", "exciting", "exquisite", "fabulous", "fair", "familiar", "famous", "fantastic", "favorable", "fetching", "fine", "fitting", "flourishing", "fortunate", "free", "fresh", "friendly", "fun", "funny", "generous", "genius", "genuine", "giving", "glamorous", "glowing", "good", "gorgeous", "graceful", "great", "green", "grin", "growing", "handsome", "happy", "harmonious", "healing", "healthy", "hearty", "heavenly", "honest", "honorable", "honored", "hug", "idea", "ideal", "imaginative", "imagine", "impressive", "independent", "innovate", "innovative", "instant", "instantaneous", "instinctive", "intellectual", "intelligent", "intuitive", "inventive", "jovial", "joy", "jubilant", "keen", "kind", "knowing", "knowledgeable", "laugh", "learned", "legendary", "light", "lively", "lovely", "lucid", "lucky", "luminous", "marvelous", "masterful", "meaningful", "merit", "meritorious", "miraculous", "motivating", "moving", "natural", "nice", "novel", "now", "nurturing", "nutritious", "okay", "one", "one-hundred percent", "open", "optimistic", "paradise", "perfect", "phenomenal", "pleasant", "pleasurable", "plentiful", "poised", "polished", "popular", "positive", "powerful", "prepared", "pretty", "principled", "productive", "progress", "prominent", "protected", "proud", "quality", "quick", "quiet", "ready", "reassuring", "refined", "refreshing", "rejoice", "reliable", "remarkable", "resounding", "respected", "restored", "reward", "rewarding", "right", "robust", "safe", "satisfactory", "secure", "seemly", "simple", "skilled", "skillful", "smile", "soulful", "sparkling", "special", "spirited", "spiritual", "stirring", "stunning", "stupendous", "success", "successful", "sunny", "super", "superb", "supporting", "surprising", "terrific", "thorough", "thrilling", "thriving", "tops", "tranquil", "transformative", "transforming", "trusting", "truthful", "unreal", "unwavering", "up", "upbeat", "upright", "upstanding", "valued", "vibrant", "victorious", "victory", "vigorous", "virtuous", "vital", "vivacious", "wealthy", "welcome", "well", "whole", "wholesome", "willing", "wonderful", "wondrous", "worthy", "wow", "yes", "yummy", "zeal", "zealous"]
negative = ["abysmal", "adverse", "alarming", "angry", "annoy", "anxious", "apathy", "appalling", "atrocious", "awful", "bad", "banal", "barbed", "belligerent", "bemoan", "beneath", "boring", "broken", "callous", "can't", "clumsy", "coarse", "cold", "cold-hearted", "collapse", "confused", "contradictory", "contrary", "corrosive", "corrupt", "crazy", "creepy", "criminal", "cruel", "cry", "cutting", "damage", "damaging", "dastardly", "dead", "decaying", "deformed", "deny", "deplorable", "depressed", "deprived", "despicable", "detrimental", "dirty", "disease", "disgusting", "disheveled", "dishonest", "dishonorable", "dismal", "distress", "don't", "dreadful", "dreary", "enraged", "eroding", "evil", "fail", "faulty", "fear", "feeble", "fight", "filthy", "foul", "frighten", "frightful", "gawky", "ghastly", "grave", "greed", "grim", "grimace", "gross", "grotesque", "gruesome", "guilty", "haggard", "hard", "hard-hearted", "harmful", "hate", "hideous", "homely", "horrendous", "horrible", "hostile", "hurt", "hurtful", "icky", "ignorant", "ignore", "ill", "immature", "imperfect", "impossible", "inane", "inelegant", "infernal", "injure", "injurious", "insane", "insidious", "insipid", "jealous", "junky", "lose", "lousy", "lumpy", "malicious", "mean", "menacing", "messy", "misshapen", "missing", "misunderstood", "moan", "moldy", "monstrous", "naive", "nasty", "naughty", "negate", "negative", "never", "no", "nobody", "nondescript", "nonsense", "not", "noxious", "objectionable", "odious", "offensive", "old", "oppressive", "pain", "perturb", "pessimistic", "petty", "plain", "poisonous", "poor", "prejudice", "questionable", "quirky", "quit", "reject", "renege", "repellant", "reptilian", "repugnant", "repulsive", "revenge", "revolting", "rocky", "rotten", "rude", "ruthless", "sad", "savage", "scare", "scary", "scream", "severe", "shocking", "shoddy", "sick", "sickening", "sinister", "slimy", "smelly", "sobbing", "sorry", "spiteful", "sticky", "stinky", "stormy", "stressful", "stuck", "stupid", "substandard", "suspect", "suspicious", "test", "terrible", "terrifying", "threatening", "ugly", "undermine", "unfair", "unfavorable", "unhappy", "unhealthy", "unjust", "unlucky", "unpleasant", "unsatisfactory", "unsightly", "untoward", "unwanted", "unwelcome", "unwholesome", "unwieldy", "unwise", "upset", "vice", "vicious", "vile", "villainous", "vindictive", "wary", "war", "weary", "wicked", "woeful", "worthless", "wound", "yell", "yucky", "zero", "reacting", "lofty", "falsified", "bust", "folded", "defaults", "bottleneck", "cloudy", "strains", "kicks", "doubted", "halving", "abandon", "depressing", "diluting"]
very_strong = ["unmatched", "outperform", "voided", "confident", "rewarded", "prosperity", "discrepancy", "rectification", "critically", "forfeitable", "arbitrary", "turmoil", "imbalance", "progresses", "antecedent", "overcharged", "duress", "manipulation", "distressed", "dissolutions", "hazard", "expropriation", "understate", "unfit", "pleadings", "investigated", "sometime", "encroachment", "misstate", "mutandis", "defraud", "undefined", "delisting", "forfeits", "uncovers", "malpractice", "presumes", "grantors", "collapsing", "falsely", "unsound", "rejections", "whereabouts", "damaging", "reassignment", "distracting", "disapproved", "stagnant", "predeceases", "unsafe"]
very_weak = ["jeopardized", "recalculate", "testify", "questionable", "impeded", "exacerbate", "overstatement", "slander", "nonperforming", "unfounded", "worst", "illicit", "renegotiate", "manipulate", "disturbing", "circumvent", "prejudiced", "apparently", "frivolous", "reject", "protested", "rejects", "downsized", "grievance", "refile", "dissenting", "foreclosed", "gratuitous", "unpredicted", "misapplication", "closeout", "collaborates", "obligee", "dissenters", "forego", "writs", "pledgors", "precipitated", "idled", "suggests", "bailee", "friendly", "arbitral", "breakthroughs", "favoring", "certiorari", "persists", "adjournments", "ignoring", "recalculate"]
neutral = ["improves", "gain", "fluctuation", "discontinue", "statutes", "thereunto", "risky", "risque", "fluctuates", "subrogation", "negatively", "lose", "attorney", "revised", "could", "exposure", "dependent", "will", "contracts", "failure", "risk", "easily", "proficiency", "supersedes", "accession", "duly", "may", "remedied", "variable", "unenforceable", "risks", "unresolved", "variations", "courts", "problem", "varied", "hereby", "predict", "favorable", "vulnerability", "claims", "alteration", "discontinuing", "bankruptcy", "depending", "depending", "attaining", "omissions", "correcting"]
influential = ["Trump", "Corona", "Virus", "Coronavirus", "COVID", "COVID19", "Tik Tok", "TikTok", "Snapchat", "China", "Iran", "army", "war"]

#Algorithm Multipliers

global positive_multiplier
global negative_multiplier
global very_strong_multiplier
global very_weak_multiplier
global neutral_multiplier
global influential_multiplier
global headline_strength
global algorithm
positive_multiplier = 0
negative_multiplier = 0
very_strong_multiplier = 0
very_weak_multiplier = 0
neutral_multiplier = 0
influential_multiplier = 0

def zero_constants():
    positive_multiplier = 0
    negative_multiplier = 0
    very_strong_multiplier = 0
    very_weak_multiplier = 0
    neutral_multiplier = 0
    influential_multiplier = 0
    headline_strength = 0
    algorithm = 0

# Setting counters to zero, in order to simplify loop processes i nthe future



#Choosing Stock
print("""
Tesla - 1

Apple - 2

Amazon - 3

Walmart - 4

Google - 5

Facebook - 6

All of the above - 0
""")

stock_pick = int(input("Enter the number next to your preferred stock from the list above, or enter \"0\" for the entire list: "))

global stock_list1
stock_list1 = []

if stock_pick == 1:
    stock_list1.append("Tesla")
elif stock_pick == 2:
    stock_list1.append("Apple")
elif stock_pick == 3:
    stock_list1.append("Amazon")
elif stock_pick == 4:
    stock_list1.append("Walmart")
elif stock_pick == 5:
    stock_list1.append("Google")
elif stock_pick == 6:
    stock_list1.append("Facebook")
elif stock_pick == 0:
    stock_list1.append("Tesla")
    stock_list1.append("Apple")
    stock_list1.append("Amazon")
    stock_list1.append("Walmart")
    stock_list1.append("Google")
    stock_list1.append("Facebook")

print("Your preferred stock has been set to the following:", "\n")
print(stock_list1,"\n")

continue1 = input("Press any key to continue. ")
print("\n")

def display_headlines():
    for cnn_headline in cnn_headlines:
        for stonk in stock_list1:
            if stonk in cnn_headline.text:
                print(cnn_headline.text)
    for forbes_headline in forbes_headlines:
        for stonk2 in stock_list1: 
            if stonk2 in forbes_headline.text:
                print(forbes_headline.text)
    for bloomberg_headline in bloomberg_headlines:
        for stonk3 in stock_list1: 
            if stonk3 in bloomberg_headline.text:
                print(bloomberg_headline.text)
    for MW_headline in MW_headlines:
        for stonk4 in stock_list1: 
            if stonk4 in MW_headline.text:
                print(forbes_headline.text)
    for WSJ_headline in WSJ_headlines:
        for stonk5 in stock_list1: 
            if stonk5 in WSJ_headline.text:
                print(WSJ_headline.text)

# Depending on the usser selected stock, respective headline scraper functions are ran 


global view_headlines
view_headlines = input("Do you want to view todays headlines for your stock(s)? Enter (Y) or (y) for yes.  ")

def news_view():
    if view_headlines == "Y" or view_headlines == "y":
        scanning()
        print("\n")
        print("HERE ARE TODAY'S HEADLINES:","\n")
        print("___________________________________________________________________________________")
        print("\n")
        display_headlines()
    else:
        scanning()
news_view()

print("\n")
print("Execute the following orders:")
print("\n")

headline_logs = open('headline_logs.csv', 'w')
headline_logs.write("HEADLINES:"+"\n")
headline_logs.close()

global decision
decision = []

def NewsBot(stock_list1):
    def cnn_algo(stock_list1):
        for x in stock_list1:
            for cnn_headline in cnn_headlines:
                if x in cnn_headline.text:
                    for y in positive:
                        if y in cnn_headline.text:
                            global positive_multiplier
                            positive_multiplier = cnn_headline.text.count(y)
                    for z in negative:
                        if z in cnn_headline.text:
                            global negative_multiplier
                            negative_multiplier = cnn_headline.text.count(z)
                    for w in very_strong:
                        if w in cnn_headline.text:
                            global very_strong_multiplier
                            very_strong_multiplier = cnn_headline.text.count(w)
                    for v in very_weak:
                        if w in cnn_headline.text:
                            global very_weak_multiplier
                            very_weak_multiplier = cnn_headline.text.count(v)
                    for u in neutral:
                        if u in cnn_headline.text:
                            global neutral_multiplier
                            neutral_multiplier = cnn_headline.text.count(u)
                    for t in influential:
                        if t in cnn_headline.text:
                            global influential_multiplier
                            influential_multiplier = cnn_headline.text.count(t)
                    headline_logs = open("headline_logs.csv", "a")
                    headline_logs.write(cnn_headline.text)
                    headline_logs.write("\n")
                    headline_logs.close()
                    headline_strength = (positive_multiplier - negative_multiplier + (very_strong_multiplier*2) - (very_weak_multiplier*2) + (neutral_multiplier) + (influential_multiplier*4) )
                    algorithm = ((headline_strength)*20)
                    if algorithm < (-5):
                        decision.append("Sell "+ str(algorithm) +" of "+ x+" shares.")
                    if algorithm > 5:
                        decision.append("Buy "+ str(algorithm) +" of "+ x+" shares.")
                    else:
                        decision.append("Hold position for "+ x+ ".")
        zero_constants()
    cnn_algo(stock_list1)
    final_decision = list(dict.fromkeys(decision))
    for x in range(len(final_decision)):    
        print(final_decision[x])

    headline_logs = open("headline_logs.csv", "a")
    headline_logs.write("\n")
    headline_logs.write("\n")
    headline_logs.write("Accessed: "+date_time)
    headline_logs.write("\n")
    headline_logs.close()


def timestamp():
    now = datetime.now()
    global date_time
    date_time = now.strftime("%H:%M:%S %m/%d/%Y")

# For future development, we can add a timestamp to log activity

timestamp()
NewsBot(stock_list1) 