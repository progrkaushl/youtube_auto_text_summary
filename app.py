import time
import streamlit as st
from api_handler import YoutubeVideoTextualSummary
from youtube_transcript_api import TranscriptsDisabled

st.set_page_config(page_title="YouTube Auto Text Summary", page_icon=":notebook:")

st.header(":notebook: YouTube Video Auto Text Summary Generator")
st.text('Pass YT video URL and automatically generate summary, notes, tasks, outlines etc.')
st.write("\n\n")

with st.expander("Read this before using", expanded=True):
    st.write("Before submitting form, please make sure below requirements are fulfilled:")
    st.markdown("- Make sure the video you are using is not `Age Restricted`.")
    st.markdown("- Make sure video has subtitles/captions enabled.")


with st.form("details_form"):
    st.write("Please provide video URL and Instruction.")

    video_url = st.text_input("YouTube Video URL:")


    instruction_text = st.text_input("What to do?", "Create summary to explain to a kid.")


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Check if YT url is provided.
        if not video_url:
            st.warning("Please provide input text.")   
            st.stop()

        if not instruction_text:
            st.warning("Please provide input text.")
            st.stop()

        st.write("Thank you for providing details.")



if video_url:
    with st.expander("Watch Video"):
        st.video(video_url) 


    with st.container():
        st.markdown("--------------")
        try:
            vid_text_completion = YoutubeVideoTextualSummary(url=video_url, instruction=instruction_text)

            with st.spinner('Please wait while your request is being processed...'):
                output_text = vid_text_completion.generate_summary()
                time.sleep(10)

                if output_text:
                    st.success('Thank you for waiting! You can check results below.', icon="✅")
                    st.write(output_text)

        except TranscriptsDisabled as err:
            st.error('Subtitles are disabled for this video. Unable to get transcipts.', icon="🚨")

        except Exception as e:
            st.error('Unkown error occured.', icon="🚨")





# Footer 
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
padding: 5px;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/kaushlendra006/" target="_blank">Kaushlendra Singh</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
