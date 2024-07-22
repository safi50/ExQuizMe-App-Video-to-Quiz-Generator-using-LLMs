-import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
import os
import sys

# Append the directory containing 'app' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.mixtral_prompts import get_quiz_prompt, get_interview_prompt
from app.mixtral_wrapper import MixtralWrapper

SAVE_DIR = './finetune_data'

# A function to choose the prompt based on the output type (Quiz / Interview)
def choose_prompt(row):
  if row['quizType'].lower() == 'quiz':
    return get_quiz_prompt(row['complexity'], row['transcription'])
  elif row['quizType'].lower() == 'interview':
    return get_interview_prompt(row['complexity'], row['transcription'])
  else:
    return row['transcription']

def prepare_data(db_path):
  # Establish connection with a SQLite database
  engine = create_engine(f'sqlite:///{db_path}')
  feedback_df = pd.read_sql_table('feedback', engine)
  
  # Load input and output values
  feedback_df['input_text'] = feedback_df.apply(choose_prompt, axis=1) # Apply filtering, so we use the right prompt
  feedback_df['target_text'] = feedback_df['quiz'].apply(lambda x: x) 
  
  # Split the data
  train_df, val_df = train_test_split(feedback_df, test_size=0.2, random_state=42)

  if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR, exist_ok=True)
  
  # Save to CSV in the specified directory
  train_df[['input_text', 'target_text']].to_csv(os.path.join(SAVE_DIR, 'train.csv'), index=False)
  val_df[['input_text', 'target_text']].to_csv(os.path.join(SAVE_DIR, 'validation.csv'), index=False)
  
  print(f"Data prepared and saved in '{SAVE_DIR}'")
  return train_df, val_df

if __name__ == '__main__':
  train_data, validation_data = prepare_data('instance/feedback.db')
  model = MixtralWrapper()
  model.fine_tune_model(SAVE_DIR)