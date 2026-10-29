def count_items(items_list):
  dict={}
  for item in items_list:
    dict[item]=dict.get(item,0)+1
  return dict
count=count_items(['apple','banana','apple','cherry','banana','apple'])
print(count)