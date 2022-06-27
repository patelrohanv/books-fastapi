import pandas as pd

# read books.csv to a pandas dataframe
allData_df = pd.read_csv('books_raw.csv',on_bad_lines='warn')
# create sets to store the data that's being pulled from the for loop
authors = set()
publishers = set()
languageCodes = set()

# loop through the allData_df and add to authors, publishers, and languageCodes
for _, row in allData_df.iterrows():
  author = row['authors']
  if '/' in author:
    bookAuthors = author.split('/')
    for ba in bookAuthors:
      authors.add(ba)
  else:
    authors.add(author)
  publishers.add(row['publisher'])
  languageCodes.add(row['language_code'])

# create dataframes for the data; using _ for dfs instead of camelcase
# output authors, publishers, and languageCodes to csv files with their index as id
authors_df = pd.DataFrame(list(authors), columns=['name'])
authors_df.to_csv('authors.csv', index_label='id')

publishers_df = pd.DataFrame(list(publishers), columns=['name'])
publishers_df.to_csv('publishers.csv', index_label='id')

languageCodes_df = pd.DataFrame(list(languageCodes), columns=['code'])
languageCodes_df.to_csv('languageCodes.csv', index_label='id')

# create lists to store the data that's being pulled from the for loop
books = [] 
booksColumns = ['id', 'title', 'average_rating', 'isbn' ,'isbn13' ,'fk_language_code' , 'num_pages', 'ratings_count', 'publication_date', 'fk_publisher']

# iterate through allData_df again
for _, row in allData_df.iterrows():
  publisherRow = publishers_df.loc[publishers_df['name'] == row['publisher']]
  languageCodeRow = languageCodes_df.loc[languageCodes_df['code'] == row['language_code']]
  books.append((
    row['id'], 
    row['title'], 
    row['average_rating'], 
    row['isbn'], 
    row['isbn13'], 
    languageCodeRow.index.item(),
    row['num_pages'],
    row['ratings_count'],
    row['publication_date'],
    publisherRow.index.item()
  ))

books_df = pd.DataFrame(books, columns=booksColumns)
books_df.set_index('id')
books_df.to_csv('books.csv', index=False)

# map books to authors
booksToAuthors= []
booksToAuthorsColumns = ['fk_bookId', 'fk_authorId']

for _, row in allData_df.iterrows():
  author = row['authors']
  if '/' in author:
    bookAuthors = author.split('/')
    for ba in bookAuthors:
      authorRow = authors_df.loc[authors_df['name'] == ba]
      booksToAuthors.append((row['id'], authorRow.index.item()))
  else:
    authorRow = authors_df.loc[authors_df['name'] == author]
    booksToAuthors.append((row['id'], authorRow.index.item()))

booksToAuthors_df = pd.DataFrame(booksToAuthors, columns=booksToAuthorsColumns)
booksToAuthors_df.to_csv('booksToAuthors.csv', index=False)