#Import Library and Modules
import time
import os, os.path
from os import listdir
from os.path import isfile, join
import numpy as np
import pandas as pd 
import sys
import re
import random
from Bio import SeqIO
from Bio import Entrez
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score,balanced_accuracy_score
from sklearn.metrics import confusion_matrix
import warnings
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import NearestCentroid
warnings.filterwarnings('ignore')

###############################################
def Change_DNA(dna):
    line = "".join(dna.split("\n")[1:])
    dna = line.upper()
    return dna
###############################################
def PC_mer(dna, k):    
    vector = 2**k #Determining the length of three vectors {weak or strong}, {amino or keto} and {purine or pyrimidine} based on k-mer size==>2^k
    start = vector // 2
    x = start

    weakStrong = [0] * (vector) #CG , AT
    aminoKeto = [0] * (vector) #AC , GT
    PurPyr = [0] * (vector) #AG , CT

    #weak or strong
    for i in range(len(dna)):
        if dna[i] == "C" or dna[i] == "G":
            x = (x + vector) // 2
            weakStrong[x] = weakStrong[x] + 1 
        
        elif dna[i] == "A" or dna[i] == "T":
            x = (x + 0) // 2
            weakStrong[x] = weakStrong[x] + 1

    x = start
    #amino or keto       
    for i in range(len(dna)):
        if dna[i] == "C" or dna[i] == "A":
            x = (x + vector) // 2
            aminoKeto[x] = aminoKeto[x] + 1 
        
        elif dna[i] == "G" or dna[i] == "T":
            x = (x + 0) // 2
            aminoKeto[x] = aminoKeto[x] + 1

    x = start
    #purine or pyrimidine
    for i in range(len(dna)):
        if dna[i] == "C" or dna[i] == "T":
            x = (x + vector) // 2
            PurPyr[x] = PurPyr[x] + 1 
        
        elif dna[i] == "A" or dna[i] == "G":
            x = (x + 0) // 2
            PurPyr[x] = PurPyr[x] + 1

    arr = np.concatenate((PurPyr, aminoKeto, weakStrong))
    return arr
###############################################
def GFL(path,k):
    ffolders = []
    dna = []
    label = []
    # define Dataset path
    mypath = path
    my_list = os.listdir(mypath)
                
    for i in range(len(my_list)):
        path = mypath + "\\" + my_list[i]
        s = os.listdir(path)
        n = len(s)
        
        for j in range(n):
            path1 = path + "\\" + s[j]
            f = open(path1 , "r")
            line = f.read()
            f.close()
            line = Change_DNA(line)
            x = PC_mer(line,k)
            dna.append(x)
            label.append(i) 
    return dna, label 
###############################################
def get_metrics(Groundtruth, Predicted):
    precision = precision_score(Groundtruth, Predicted, average='weighted')
    recall = recall_score(Groundtruth, Predicted, average='weighted')
    f1 = f1_score(Groundtruth, Predicted, average='weighted')
    acc=accuracy_score(Groundtruth, Predicted)
    return precision, recall, f1, acc

###############################################

def comp_confmat(Groundtruth, Predicted):
    classes = np.unique(Groundtruth) # extract the different classes
    matrix = np.zeros((len(classes), len(classes))) # initialize the confusion matrix with zeros
    for i in range(len(classes)):
        for j in range(len(classes)):
            matrix[i, j] = np.sum((Groundtruth == classes[i]) & (Predicted == classes[j]))
    return matrix

###############################################
def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure(figsize=(10, 10))
    csfont = {'fontname':'Times New Roman'}
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title,fontsize=20,weight='bold',**csfont)

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=70,fontsize=10,**csfont)
        plt.yticks(tick_marks, target_names,fontsize=10,**csfont)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]


    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")


            
    plt.tight_layout()
    plt.ylabel('True label',fontsize=15,**csfont)
    plt.xlabel('Predicted label',fontsize=15,**csfont)
    plt.savefig('AMPClass.png',dpi=350,bbox_inches = 'tight',
    pad_inches = 0.5)
    plt.show()
    
###############################################

def train(PCmer_features, label, folds, clf):
   
    X=np.array(PCmer_features)
    y=np.array(label)
    kfold = folds
    sumSen = 0
    sumSpec = 0
    sumP = 0
    sumR = 0
    sumF = 0
    sumacc=0
    sumaccbl=0
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'CM')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    skf = StratifiedKFold(n_splits=kfold,shuffle=True,random_state=20)
    t1 = time.time()
    tempfold=1
    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        if clf=='LR':
            clf = LogisticRegression().fit(X_train, y_train)
        elif clf=='SVC':
            clf = make_pipeline(StandardScaler(), SVC(kernel='linear')).fit(X_train, y_train)
        elif clf=='GNB':
            clf = GaussianNB().fit(X_train, y_train)
        elif clf=='LDA':
            clf = LinearDiscriminantAnalysis().fit(X_train, y_train)
        elif clf=='DT':
            clf = DecisionTreeClassifier().fit(X_train, y_train)
        elif clf=='MLP':
            clf = MLPClassifier().fit(X_train, y_train)


        y_pred = clf.predict(X_test)
        cm=comp_confmat(y_test,y_pred)
        np.savetxt('CM/'+'CM_fold'+str(tempfold)+'.txt',cm)
        f = open("Report.txt", "a")
        f.write("Fold"+str(tempfold)+':\n')
        precision, recall, f1,acc = get_metrics(y_test, y_pred)
        f.write("precision:"+str(precision)+'\n')
        f.write("recall:"+str(recall)+'\n')
        f.write("f1:"+str(f1)+'\n')
        f.write("acc:"+str(acc)+'\n')
        sumP = sumP + precision
        sumR = sumR + recall
        sumF = sumF + f1
        sumacc=sumacc+acc
        f.close()
        tempfold=tempfold+1

    finalPrec = sumP/kfold
    finalRcl = sumR/kfold
    finalF = sumF/kfold
    finalacc=sumacc/kfold
    t2 = time.time()
    totalTime = t2 - t1
    print("time = %.2f"  %(totalTime))
    print("accuracy = %.3f" %(finalacc))
    print("precision = %.3f \nrecall = %.3f \nf1 = %.3f" %(finalPrec, finalRcl, finalF))
###############################################
def pcmer_api(fname,seqid):
    Entrez.email = "https://pubmed.ncbi.nlm.nih.gov/"  
    filename = fname
    if not os.path.isfile(filename):
        # Downloading...
        net_handle = Entrez.efetch(
            db="nucleotide", id=seqid, rettype="fasta", retmode="text"
        )
        out_handle = open(filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")

    print("Parsing...")
    record = SeqIO.read(filename, "fasta")
    print(record)
