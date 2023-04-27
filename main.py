import imagerec
p = imagerec.imagerecognise("ValidationTesting/imgNormal.jpeg","Models/FinalModel.h5","Models/labels.txt")
print(f"FINAL - {p}")