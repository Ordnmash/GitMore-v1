def sample(nums): # this function is used to ask the model to generate the commits like, it works well
  
  for i in range(nums):
    out = []
    context = [0] * block_size
    
    while True:
      
      contx  = torch.tensor([context])
      logits = model(contx)
      probs  = F.softmax(logits, dim=1)
      ix     = torch.multinomial(probs, num_samples=1, replacement=True).item()
    
      if ix == 0: # because 0 is the special ENDtoken we want to break assuming the model predicts the sentence comes to an end.
        break
      
      else:
        out.append(itos[ix])
        context = context[1:] + [ix]
    
    print(''.join(out))
    print("") # print empty string to have spacing when the model sample nums > 1
    
# to search whether the model is getting some words type from the data or it's just making them up
def search(x: str):
  count= 0
  cont = []
  
  for c in commits:
    if x.lower() in c.lower():
      cont.append(c)
      count+=1
  
  print(f'{count} matches found...')
  return cont if cont else None
