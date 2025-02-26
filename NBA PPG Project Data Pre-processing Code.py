# Load the pre-processed data
data = pd.read_csv('2023-2024 NBA Player Stats - Regular 2.csv', encoding='latin-1')

# Subset of Players
subset_players = [
   'Trae Young', 'Dejounte Murray', 'Ben Simmons', 'Jayson Tatum', 'Jaylen Brown', 'LaMelo Ball', 'DeMar DeRozan',
   'Zach LaVine', 'Nikola Vucevic', 'Donovan Mitchell', 'Jarrett Allen', 'Darius Garland', 'Luka Doncic',
   'Kyrie Irving', 'Nikola Jokic', 'Stephen Curry', 'Draymond Green', 'Andrew Wiggins', 'Chris Paul',
   'Fred VanVleet', 'Tyrese Haliburton', 'Kawhi Leonard', 'Paul George', 'LeBron James', 'Anthony Davis',
   'Jaren Jackson Jr.', 'Jimmy Butler', 'Bam Adebayo', 'Giannis Antetokounmpo', 'Jrue Holiday', 'Khris Middleton',
   'Rudy Gobert', 'Karl-Anthony Towns', 'Mike Conley', 'Anthony Edwards', 'Zion Williamson', 'Julius Randle',
   'Shai Gilgeous-Alexander', 'Joel Embiid', 'James Harden', 'Bradley Beal', 'Devin Booker', 'Kevin Durant',
   'Damian Lillard', 'Domantas Sabonis', 'De'Aaron Fox', 'Pascal Siakam', 'Lauri Markkanen'
]

# Filter the dataset for the subset of players
subset_data = data[data['Player'].isin(subset_players)]

# 'Rk' is not used in the model calculation
X = subset_data['Player', 'FGA', 'FG%', '3P', '3PA', '3P%', 'eFG%', 'FTA', 'FT%']]
Y = subset_data['PTS']

# Encode categorical variables
label_encoder = LabelEncoder()
X['Player'] = label_encoder.fit_transform(X['Player'])
