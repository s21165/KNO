from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

syn0 = wn.synsets('forest')[0]
syn1 = wn.synsets('tree')[0]
syn2 = wn.synsets('brown')[0]
syn3 = wn.synsets('yellow')[0]
syn4 = wn.synsets('animals')[0]
syn5 = wn.synsets('mushroom')[0]
syn6 = wn.synsets('walk')[0]
syn7 = wn.synsets('leaf')[0]
syn8 = wn.synsets('deer')[0]
syn9 = wn.synsets('rowan')[0]

all_syn = [syn0, syn1, syn2, syn3, syn4, syn5, syn6, syn7, syn8, syn9]

print("Synset names")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset name: {all_syn[idx].name()}")
    print("-----")

print("\nSynset definitions")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset definition: {all_syn[idx].definition()}")

print("\nSynset examples")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset examples: {all_syn[idx].examples()}")

print("\nSynset abstract terms")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset abstract term: {all_syn[idx].hypernyms()}")

print("\nSynset hyponymus")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset hyponumys: {all_syn[idx].hyponyms()}")

print("\nSynset specific terms")
for idx in range(len(all_syn)):
    print(f"{idx + 1}. Synset specific term: {all_syn[idx].hypernyms()[0].hyponyms()}")

print("\n Synsets similarity")
for syn_x in all_syn[:3]:
    for syn_y in all_syn:
        print(f"{syn_x} with {syn_y}")
        print(syn_x.wup_similarity(syn_y))


def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()

    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name())
            for s1 in fn(s):
                graph.add_node(s1.name())
                graph.add_edge(s.name(), s1.name())
                recurse(s1)
    recurse(synset)
    return graph


for word in all_syn:
    nx.draw_networkx(closure_graph(wn.synset(word.name()), lambda s: s.hypernyms()))
    plt.show()