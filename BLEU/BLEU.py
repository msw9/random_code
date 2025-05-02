import nltk
"""
documentation pour SmoothingFunction()
https://www.nltk.org/api/nltk.translate.bleu_score.html#nltk.translate.bleu_score.SmoothingFunction
"""
with open("mes_resultats.txt", encoding="utf-8") as f:
    candidates = f.readlines()
with open("corrige.txt", encoding="utf-8") as f:
    references = f.readlines()
with open("notes.txt",mode="r+",encoding="utf-8") as f:
    f.seek(0)
    f.truncate()
    
smooth = nltk.translate.bleu_score.SmoothingFunction()
candidates = [line.strip() for line in candidates]
references = [line.strip() for line in references]

# Error proof
if len(references) != len(candidates):
    raise ValueError("Le nombre de références et de candidats doit être le même.")

# Calcul BLEU
for ref, cand in zip(references, candidates):
    # Les références doivent être une liste de listes
    ref_list = [ref.split()]
    cand_list = cand.split()
    bleu_score = nltk.translate.bleu_score.sentence_bleu(ref_list, cand_list,smoothing_function= smooth.method1)
    with open ("notes.txt",mode="a+", encoding="utf-8") as f:
        f.write(f"{str(bleu_score)}\n")
