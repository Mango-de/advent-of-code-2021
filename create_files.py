import sys, os, requests, dotenv

dotenv.load_dotenv()

_, year, day = sys.argv

result = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': os.environ['SESSION_TOKEN']})

for l in result.text.split('\n')[:5]:
    print(l)
print('...')

with open(f'inputs/{day}', 'w') as f:
    f.write(result.text[:-1])
    
with open(f'solutions/{day}.py', 'w') as f:
    f.write(
f'''with open('inputs/{day}') as f:
    l = [int(x) for x in f]
    l = f.read().splitlines() # if you don't have digits

# Part 1



# Part 2

'''
    )