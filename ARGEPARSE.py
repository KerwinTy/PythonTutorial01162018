import argparse
parser = argparse.ArgumentParser()
parser.add_argument("arianne")
args = parser.parse_args()
print(args.arianne)

if args.arianne == "Maganda":
    print ("Panget ako")
elif args.arianne == "Mataray":
    print ("Tru")
else:
    print ("Manlilibre ako")