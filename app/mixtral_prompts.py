def get_quiz_prompt(complexity, transcription):
  prompt = (f"Generate a {complexity}-level comprehensive quiz based on the following key concepts described in the transcription: \"{transcription}\". "
    "The quiz should consist of questions that test understanding of concepts of the main topics rather than specifics mentioned in the transcription. "
    "Each question should come with four options (A, B, C, D), with only one correct answer. "
    "Please provide the quiz in JSON format, ensuring a clear distinction between the question, options, and the correct answer. Example of expected format: "
    "{'question': 'How many predictor variables are in simple linear regression?', "
    "'options': ['A) One', 'B) Two', 'C) Five or more', 'D) Ten or more'], "
    "'answer': 'A) One'}. JSON Quiz Output:\n")

  return [
    {"role": "user", "content": prompt},
  ]


def get_interview_prompt(complexity, transcription):
  prompt = (f"Generate a {complexity}-level comprehensive job-interview questions based on the following key concepts described in the transcription: \"{transcription}\". "
    "The interview questions should consist of questions that test understanding of concepts of the main topics rather than specifics mentioned in the transcription. "
    "Each question should come with a comprehensive answer. "
    "Please provide the quiz in JSON format, ensuring a clear distinction between the question and the answer. Example of expected format: "
    "{'question': 'Does correlation imply causation? Can you explain it with some examples?', "
    "'answer': 'No, correlation does not imply causation. Correlation simply measures the degree of association between two variables, while causation indicates that one variable directly affects the other. For instance, ice cream sales and heat strokes are positively correlated in the summer, but selling more ice cream doesn't cause more heat strokes. Both variables are influenced by a third factor, which is the hot weather. Another example is the correlation between umbrella sales and rainfall. Umbrella sales may increase when it rains, but selling umbrellas doesn't cause the rain.'}. JSON Quiz Output:\n")

  return [
    {"role": "user", "content": prompt},
  ]


def get_correction_prompt(text_chunk):
  prompt =  (f"Correct any typos, misspellings, especially in brand names and proper names, in the text below."
            f"Do not add any extra text or commentary; just provide the corrected version of the text:\n\n" 
            f"'''\n{text_chunk}\n'''")
  return [{"role": "user", "content": prompt},]