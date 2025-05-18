#add import

from src.question_a.question_a import get_most_likely_ancestor_consensus

def main():
   while True:
      dna_string1 = input("Please enter a DNA string of 9-15 characters:").upper()
      if not (8 < len(dna_string1) <= 16):
         print("Invalid, please try again.")
         continue
      
      dna_string2 = input("Please enter a DNA substring of 4 characters:").upper()
      if len(dna_string2) != 4:
         print("Invalid, please try again.")
         continue
      
      result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
      if result:
         print("Substring found at positions:", *result)
      else:
         print("Substring not found.")

      try_again = input("Would you like to try again? (y/n):")
      if try_again.lower() != 'y':
         break

if __name__ == "__main__":
   main()   