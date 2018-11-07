import Algorithmia

input = "Cut the bread into slices with the knife. Take one slice and then put butter on it. Add honey on it later. "
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('StanfordNLP/DeterministicCoreferenceResolution/0.1.1')
print(algo.pipe(input).result)
