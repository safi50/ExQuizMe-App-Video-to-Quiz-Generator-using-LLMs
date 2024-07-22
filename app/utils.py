import yaml

def parse_json_output(quiz_text, retries = 5):
  """
  Parses the JSON output of a model.
  Returns a parsed list of dictionaries.
  """
  try:
      cleaned_quiz_json = clean_json_string(quiz_text)
      return yaml.safe_load(cleaned_quiz_json)
  except Exception as e:
      # Handle parsing error
      print(f"Parse quiz output error: {e}")
      if retries > 0:
          return parse_json_output(quiz_text, retries - 1)
      return {"error": "Failed to parse quiz output from the model."}


def clean_json_string(s):
  """
  Cleans a JSON string if it's incomplete. 
  This function is used when the model returns an incomplete JSON object at the end of the execution.
  """
  # We start from the end of the string and move backwards
  for i in range(len(s) - 1, -1, -1):
      # If we find a '}' or ']', we stop and keep everything up to this point
      if s[i] == '}' or s[i] == ']':
          return s[:i+1]
  # If no '}' or ']' is found, return the original string
  return s

def chunk_transcription(tokenizer, transcription, max_chunk_size):
  """
  Chunks and tokenizes each word  in the given transcription. 
  Returns  a list of chunks where each chunk is a list of tokens.
  """
  splitted_transcription = transcription.split(" ")
  queue = [[]]
  index = 0

  for token in splitted_transcription:
      if len(tokenizer.tokenize(' '.join([token] + queue[index]))) < max_chunk_size:
          queue[index].append(token)
      else:
          index += 1
          queue[index].append(token)

  return queue