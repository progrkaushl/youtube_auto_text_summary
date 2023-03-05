import openai
import requests
from bs4 import BeautifulSoup
from operator import itemgetter
from youtube_transcript_api import YouTubeTranscriptApi
from utils import lang_model_output



class YoutubeVideoTextualSummary:
    
    def __init__(self, url, instruction):
        self.url = url
        self.instruction = instruction
        
    def get_video_id(self):
        print("Processing Youtube Video: ", self.url)
        
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        metas = soup.find_all('meta')
        video_id = [meta.attrs['content'] for meta in metas if 'itemprop' in meta.attrs and meta.attrs['itemprop'] == "videoId"]

        return ''.join(video_id) if len(video_id) > 0 else None
            
        
    def get_video_transcript(self):
        video_id = self.get_video_id()
        
        if video_id:
            print("Getting video transcript....")
            transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = ' '.join(list(map(itemgetter('text'), transcript_data)))
            
        return transcript_text if transcript_data else None   
    
    
    def generate_summary(self):
        input_text = self.get_video_transcript()
        instruction = self.instruction
        
        if not input_text:
            print("No input text available to perform instruction...")
            return None
        
        if instruction:
            prompt_text = '{0}\nUsing Text:\n{1}'.format(instruction, input_text)
        else:
            prompt_text = input_text
        
        # Get response
        print("Processing request....")
        response = lang_model_output(prompt_text=prompt_text)
        
        return response