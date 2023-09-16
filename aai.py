import assemblyai as aai

# replace with your API token
aai.settings.api_key = f"76eac9051cef45c9b314043224f6e194"

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

config = aai.TranscriptionConfig(iab_categories=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

# Get the parts of the transcript that were tagged with topics
for result in transcript.iab_categories.results:
  print(result.text)
  print(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}")
  for label in result.labels:
    print(label.label)  # topic
    print(label.relevance)  # how relevant the label is for the portion of text

# Get a summary of all topics in the transcript
for label, relevance in transcript.iab_categories.summary.items():
  print(f"Audio is {relevance * 100}% relevant to {label}")
