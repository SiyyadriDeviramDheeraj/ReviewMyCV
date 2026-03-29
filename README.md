# ReviewMyCV
ReviewMyCV is a tool I built to help people understand exactly how well their resume matches a job description. Instead of just guessing, it uses logic to find where your skills overlap and where you might have gaps that need filling.

What it actually does
Catches bad uploads
I noticed that many resumes are actually images or "scanned" files that computers can't read. I added a layer that detects this immediately, so the user knows they need to upload a text-based version instead of getting a broken result.

Smart matching
The app doesn't just look for exact words. I built it to understand that if a job asks for Web Frontend and you have Next.js on your resume, that is a match. It groups these skills together to give a much fairer and more accurate score.

Instant reports
I wanted users to be able to save their progress, so the app creates a professional analysis report as a PDF. It does this entirely in the moment without saving any of your personal data anywhere, keeping everything private.

Ready to test
To make it easy for anyone to see how it works, I included a set of sample resumes and job posts right in the app. You can download them and run the analysis in seconds to see the logic in action.

The technology behind it
I built the interface using Streamlit and customized it with a clean green theme. The "brain" of the app runs on Python, specifically using tools like PyPDF2 to read the files and FPDF to create the final reports.

How to get started
You just upload your resume, paste the job details, and hit analyze. Once you see your score and the missing skills, the app gives you a custom prompt that you can use with an AI to help rewrite your bullet points or prep for the interview.

Created by Deviram Dheeraj
