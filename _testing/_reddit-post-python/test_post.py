#ref: https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
'''
    libraries
        $ pip install praw
        $ pip install json
        $ pip install requests
'''

import json
import praw
from praw.models import InlineGif, InlineImage, InlineVideo
import requests

## note_022723: sub 'pythonsandlot' requires approval to post
#subr = 'pythonsandlot'
#title = 'Just Made My first Post on Reddit Using Python.'
#selftext = 'that was easy'

## note_022723: sub 'floki' requires flair to post (can't get working yet)
#subr = 'floki'
#title = 'Floki Locker?'
#selftext = 'hello, does anyone have information on floki locker. specifically i am looking for integratoin details or perhaps a whitepaper that describes how floki locker works under the hood. I am attemtping to confirm whether or not 3rd party trust is required, or if it is trustless and completely automated. thanks!'
#flair = 'educative'
#flair = None
#flair_id = '6'

## note_022723: successful!
subr = 'test'
title = 'test g post img 10 png'
#title = 'test un'
#selftext = 'that was easy'
#image = InlineImage(path="test_jpg.jpg", caption="")
image = InlineImage(path="test_png.png", caption="")
#image = InlineImage(path=f"../../public/images/{img_name}.png", caption="")
media = {"image1": image}
selftext = '''
A HNW family, living on the UES, is looking to hire a Bookkeeper/PA to care for financial bookkeeping and assistant needs. Job requires good experience, at ease with Excel and other Office applications, doing payroll. Responsibilities include: use Word and Excel, handle all email, manage schedule and social calendar, keep inventory, handle all correspondence, follow up promptly, multi-task.\n\nAll candidates are expected to be legal to work, be tech savvy, be computer savvy, have neat presentation, be college-educated, speak excellent English, love kids

    {image1}
'''

# get json file
credentials = 'client_secrets.json'
with open(credentials) as f:
    creds = json.load(f)

# get vals from json file
client_id=creds['client_id']
client_secret=creds['client_secret']
user_agent=creds['user_agent']
redirect_uri=creds['redirect_uri']
refresh_token=creds['refresh_token']
username=creds['username']
password=creds['password']
#selftext = creds['selftext']

# use refresh_token: successful testing
#ref: https://www.jcchouinard.com/post-on-reddit-api-with-python-praw/
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    redirect_uri=redirect_uri,
    refresh_token=refresh_token
)
 
# use un / pw: unsuccessful testing
#ref: https://pypi.org/project/praw/
#reddit = praw.Reddit(
#    client_id=client_id,
#    client_secret=client_secret,
#    username=username,
#    user_agent=user_agent,
#    password=password
#)

# connect / autenticate
subreddit = reddit.subreddit(subr)

# get / select flair
print('printing flair templates...')
flair_id = None
fair_text = None
for i,v in enumerate(subreddit.flair.link_templates):
    print(f'index: {i}; value: {v}')
    if v['text'] == fair_text and fair_text is not None:
        print(f'found text: {fair_text} w/ id: {v["id"]}')
        flair_id = v['id']
        break

print(f'submitting post... w/ flair_id: {flair_id}')
submission = subreddit.submit(title,inline_media=media,selftext=selftext,flair_id=flair_id)

# check / print attributes for given object -> vars(submission)
#   i.e. reddit can change these at any time
#ref: https://praw.readthedocs.io/en/latest/getting_started/quick_start.html#determine-available-attributes-of-an-object
import pprint
# assume you have a praw.Reddit instance bound to variable `reddit`
#submission = reddit.submission("39zje0")
print('submission.title => ' +submission.title)  # to make it non-lazy
pprint.pprint(vars(submission))
print(f'\n\nsubmission.url => {submission.url}')

# post
#subreddit.submit(title,selftext=selftext)
#subreddit.submit(title,selftext=selftext,flair_id=flair)
#subreddit.submit(title,inline_media=media,selftext=selftext)
#subreddit.submit(title,inline_media=media)

#ref: https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html#praw.models.Subreddit.submit_image
#gif = InlineGif(path="path/to/image.gif", caption="optional caption")
#image = InlineImage(path="path/to/image.jpg", caption="optional caption")
#video = InlineVideo(path="path/to/video.mp4", caption="optional caption")
#media = {"gif1": gif, "image1": image, "video1": video}
#reddit.subreddit("test").submit("title", inline_media=media, selftext=selftext)

