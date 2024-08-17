import pprint
import re
import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from functools import partial
import time
from typing import List, Tuple

# Constants for bookmark patterns
BOOKMARK_PATTERN = re.compile(r'<DT><A HREF="(.*?)" ADD_DATE="(\d+)"[^>]*>(.*?)</A>')
FOLDER_PATTERN = re.compile(r'>([^>]+)</H3>')

def process_bookmark_chunk(chunk: List[str], chunk_index: int) -> List[Tuple[str, str, str]]:
    """
    Processes a chunk of the bookmark HTML content and extracts bookmark and folder information.
    Args: chunk (List[str]): A list of lines representing a chunk of the HTML file, chunk_index (int): The index of the chunk being processed.
    Returns: List[Tuple[str, str, str]]: A list of extracted bookmarks from the chunk.
    """
    bookmarks: List[Tuple[str, str, str]] = []
    for line in tqdm(chunk, desc=f"Processing chunk {chunk_index + 1}", position=chunk_index, leave=True):
        # Extract bookmarks
        bookmark_matches = BOOKMARK_PATTERN.search(line)
        if bookmark_matches:
            bookmarks.append(
                (
                    bookmark_matches[1],  # URL
                    bookmark_matches[2],  # Add date
                    bookmark_matches[3].strip(),  # Title
                )
            )
        time.sleep(0.01)  # Simulate processing time
    return bookmarks

def chunk_file(file_path: str, num_chunks: int = 4) -> List[List[str]]:
    """
    Splits the file into chunks for parallel processing.
    Args: file_path (str): The path to the bookmark HTML file, num_chunks (int): Number of chunks to split the file into.
    Returns: List[List[str]]: A list containing file chunks.
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()
        chunk_size = len(lines) // num_chunks
        return [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

def process_file_in_parallel(file_path: str, num_chunks: int = 4) -> pd.DataFrame:
    """
    Processes the bookmark file in parallel using multiple processes.
    Args: file_path (str): The path to the bookmark HTML file, num_chunks (int): Number of chunks to split the file into for parallel processing.
    Returns: pd.DataFrame: A DataFrame containing all processed bookmarks.
    """
    # Split the file into chunks
    chunks = chunk_file(file_path, num_chunks=num_chunks)

    # Create a multiprocessing Pool and process the chunks in parallel
    with Pool(processes=min(cpu_count(), num_chunks)) as pool:
        # Use partial to pass the chunk index
        results = pool.starmap(partial(process_bookmark_chunk), [(chunks[i], i) for i in range(num_chunks)])

    # Flatten the list of results
    bookmarks = [bookmark for sublist in results for bookmark in sublist]
    
    # Convert to DataFrame
    return pd.DataFrame(bookmarks, columns=['URL', 'Date Modified', 'Name'])

def rename_and_detect_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renames bookmarks and detects duplicates based on specific patterns using vectorized operations.
    Args: df (pd.DataFrame): DataFrame containing bookmark information.
    Returns: pd.DataFrame: Updated DataFrame with renamed bookmarks and duplicate flags.
    """
    # Define patterns
    youtube_subscription_pattern = re.compile(r'\(\d+\)')
    youtube_label_pattern = re.compile(r' - YouTube')
    google_label_pattern = re.compile(r' - Google Search')

    # Vectorized operations for renaming
    df['Name'] = df['Name'].str.replace(youtube_subscription_pattern, "", regex=True)
    df['Name'] = df['Name'].str.replace(youtube_label_pattern, "", regex=True)
    df['Name'] = df['Name'].str.replace(google_label_pattern, "", regex=True)

    # Detect duplicates using efficient data structures (sets)
    df['Duplicate Name'] = df.duplicated(subset='Name')
    df['Duplicate URL'] = df.duplicated(subset='URL')

    return df

def save_to_csv(df: pd.DataFrame, output_file: str) -> None:
    """
    Saves the DataFrame to a CSV file.
    Args: df (pd.DataFrame): DataFrame containing bookmark information, output_file (str): The path to the output CSV file.
    """
    df.to_csv(output_file, index=False)
    print(f"Bookmarks saved to {output_file}")

def main():
    # Path to the bookmark HTML file
    file_path = "C:/Users/ishaa/Coding Projects/Python-Scripts/Bookmarks Sorter/test.html"
    output_file = "bookmarks.csv"

    # Process the bookmark file in parallel
    bookmark_df = process_file_in_parallel(file_path, num_chunks=4)

    time.sleep(0.3)  # Simulate processing time
    # Rename and detect duplicates
    bookmark_df = rename_and_detect_duplicates(bookmark_df)

    # Save the DataFrame to CSV
    save_to_csv(bookmark_df, output_file)

    # Pretty print the bookmarks for debugging purposes
    pprint.pprint(bookmark_df.head())

if __name__ == "__main__":
    main()
