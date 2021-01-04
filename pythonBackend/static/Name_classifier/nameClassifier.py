import numpy as np

DIMS=256


pos, neg, posprob, negprob = 0.5, 0.5, np.array([0.00830565, 0.04651163, 0.00664452, 0.01162791, 0.00332226,
       0.02657807, 0.01328904, 0.00498339, 0.01328904, 0.00996678,
       0.00498339, 0.02491694, 0.00332226, 0.00332226, 0.00664452,
       0.01827243, 0.01328904, 0.00166113, 0.99833887, 0.03156146,
       0.12458472, 0.00498339, 0.00332226, 0.00996678, 0.00830565,
       0.02159468, 0.00664452, 0.00830565, 0.00830565, 0.02325581,
       0.00498339, 0.01162791, 0.02325581, 0.01162791, 0.00498339,
       0.00332226, 0.01328904, 0.00498339, 0.00332226, 0.00498339,
       0.00664452, 0.00830565, 0.01827243, 0.01162791, 0.00332226,
       0.0166113 , 0.00332226, 0.00332226, 0.00498339, 0.01162791,
       0.00332226, 0.00830565, 0.00332226, 0.01495017, 0.01495017,
       0.00498339, 0.00664452, 0.01827243, 0.00830565, 0.00996678,
       0.00664452, 0.01993355, 0.00830565, 0.00166113, 0.00664452,
       0.00498339, 0.0448505 , 0.01495017, 0.01162791, 0.01495017,
       0.00498339, 0.01162791, 0.01993355, 0.0166113 , 0.00498339,
       0.02159468, 0.03488372, 0.00498339, 0.00996678, 0.02491694,
       0.01827243, 0.00332226, 0.00664452, 0.00332226, 0.03488372,
       0.00996678, 0.00830565, 0.00664452, 0.01827243, 0.01328904,
       0.03322259, 0.00332226, 0.01162791, 0.02491694, 0.00830565,
       0.0166113 , 0.05980066, 0.02159468, 0.08803987, 0.02159468,
       0.02159468, 0.00332226, 0.00498339, 0.00664452, 0.06146179,
       0.07807309, 0.0166113 , 0.01993355, 0.02990033, 0.01495017,
       0.02325581, 0.0448505 , 0.0730897 , 0.13787375, 0.02325581,
       0.03156146, 0.0166113 , 0.0448505 , 0.06976744, 0.04318937,
       0.08139535, 0.06146179, 0.09302326, 0.01162791, 0.04651163,
       0.02657807, 0.08803987, 0.09302326, 0.05481728, 0.00332226,
       0.01328904, 0.0282392 , 0.01162791, 0.05149502, 0.03488372,
       0.0166113 , 0.00830565, 0.00664452, 0.00498339, 0.07475083,
       0.01328904, 0.01827243, 0.00830565, 0.02325581, 0.01827243,
       0.00664452, 0.01162791, 0.01162791, 0.02159468, 0.01495017,
       0.01495017, 0.00664452, 0.0166113 , 0.00830565, 0.01495017,
       0.01993355, 0.01993355, 0.02159468, 0.09634551, 0.01827243,
       0.33554817, 0.07807309, 0.06146179, 0.02491694, 0.00498339,
       0.03322259, 0.03322259, 0.04817276, 0.00664452, 0.01162791,
       0.04817276, 0.12126246, 0.0166113 , 0.04152824, 0.00830565,
       0.01495017, 0.00498339, 0.00996678, 0.00166113, 0.00830565,
       0.00664452, 0.00664452, 0.00996678, 0.08803987, 0.00332226,
       0.00830565, 0.03156146, 0.01993355, 0.08305648, 0.07475083,
       0.00996678, 0.01162791, 0.00332226, 0.00498339, 0.00498339,
       0.01827243, 0.0166113 , 0.00498339, 0.01162791, 0.00830565,
       0.00332226, 0.01328904, 0.00664452, 0.00664452, 0.00664452,
       0.02491694, 0.02325581, 0.01162791, 0.00664452, 0.02491694,
       0.00996678, 0.03488372, 0.01162791, 0.00996678, 0.01162791,
       0.01328904, 0.01827243, 0.00830565, 0.00830565, 0.03322259,
       0.00664452, 0.01328904, 0.01162791, 0.00830565, 0.00830565,
       0.00996678, 0.00664452, 0.01162791, 0.0166113 , 0.00830565,
       0.00830565, 0.01162791, 0.00332226, 0.00664452, 0.00664452,
       0.00498339, 0.00830565, 0.0166113 , 0.00498339, 0.00996678,
       0.00664452, 0.00332226, 0.01495017, 0.00166113, 0.00996678,
       0.00830565, 0.00830565, 0.00498339, 0.00830565, 0.00830565,
       0.05481728, 0.00498339, 0.00166113, 0.00664452, 0.00830565,
       0.00332226]), np.array([0.00332226, 0.02325581, 0.00332226, 0.00830565, 0.00664452,
       0.02159468, 0.02657807, 0.00664452, 0.00664452, 0.01162791,
       0.00166113, 0.01162791, 0.00498339, 0.00498339, 0.00332226,
       0.01827243, 0.00664452, 0.00830565, 0.99833887, 0.01993355,
       0.03322259, 0.00664452, 0.00664452, 0.02657807, 0.00166113,
       0.00332226, 0.02491694, 0.00664452, 0.00664452, 0.00498339,
       0.00996678, 0.01328904, 0.00166113, 0.00830565, 0.00332226,
       0.00498339, 0.00166113, 0.00996678, 0.00830565, 0.00498339,
       0.00664452, 0.01328904, 0.00830565, 0.00332226, 0.00332226,
       0.03156146, 0.02159468, 0.00332226, 0.00498339, 0.03654485,
       0.00332226, 0.00664452, 0.00664452, 0.02491694, 0.01993355,
       0.01495017, 0.00664452, 0.01993355, 0.00830565, 0.00830565,
       0.00664452, 0.02159468, 0.00830565, 0.00996678, 0.00166113,
       0.00166113, 0.03654485, 0.00332226, 0.01495017, 0.00830565,
       0.06644518, 0.00830565, 0.02325581, 0.00830565, 0.0166113 ,
       0.01495017, 0.05647841, 0.00498339, 0.01827243, 0.01162791,
       0.01993355, 0.02159468, 0.00664452, 0.00332226, 0.04318937,
       0.01162791, 0.00498339, 0.01162791, 0.01162791, 0.01993355,
       0.00996678, 0.00498339, 0.01162791, 0.00996678, 0.01495017,
       0.01495017, 0.02325581, 0.0166113 , 0.04318937, 0.01328904,
       0.03322259, 0.00830565, 0.00664452, 0.00498339, 0.07807309,
       0.06478405, 0.01495017, 0.02990033, 0.01328904, 0.03156146,
       0.00996678, 0.03488372, 0.09136213, 0.08305648, 0.02657807,
       0.03488372, 0.00498339, 0.07807309, 0.14285714, 0.07973422,
       0.06644518, 0.05980066, 0.16445183, 0.00166113, 0.03322259,
       0.01162791, 0.06478405, 0.05647841, 0.03488372, 0.00498339,
       0.00996678, 0.00996678, 0.01827243, 0.02990033, 0.0166113 ,
       0.00332226, 0.00830565, 0.0730897 , 0.00830565, 0.04318937,
       0.00664452, 0.05813953, 0.00332226, 0.0166113 , 0.00498339,
       0.00664452, 0.00498339, 0.00996678, 0.00332226, 0.00830565,
       0.00498339, 0.00830565, 0.1013289 , 0.00830565, 0.00498339,
       0.01328904, 0.00498339, 0.01162791, 0.02491694, 0.01495017,
       0.14119601, 0.00332226, 0.03322259, 0.02325581, 0.00332226,
       0.00332226, 0.06976744, 0.04318937, 0.00664452, 0.01827243,
       0.00830565, 0.18936877, 0.00830565, 0.00996678, 0.00664452,
       0.40697674, 0.01495017, 0.01162791, 0.00498339, 0.00498339,
       0.00664452, 0.00166113, 0.00664452, 0.11960133, 0.00996678,
       0.00996678, 0.01328904, 0.00664452, 0.01993355, 0.02159468,
       0.00498339, 0.01495017, 0.00830565, 0.00664452, 0.00332226,
       0.01328904, 0.0166113 , 0.00996678, 0.00830565, 0.01827243,
       0.00498339, 0.00664452, 0.02159468, 0.00332226, 0.00664452,
       0.02159468, 0.01495017, 0.02325581, 0.01328904, 0.03986711,
       0.02159468, 0.05980066, 0.00664452, 0.01495017, 0.00996678,
       0.00996678, 0.03488372, 0.00830565, 0.00996678, 0.03322259,
       0.12458472, 0.0166113 , 0.00332226, 0.00830565, 0.00664452,
       0.00498339, 0.00830565, 0.01162791, 0.00996678, 0.00830565,
       0.00498339, 0.01162791, 0.00498339, 0.00332226, 0.00664452,
       0.00498339, 0.00830565, 0.01162791, 0.00498339, 0.00664452,
       0.00498339, 0.00498339, 0.02657807, 0.00830565, 0.00996678,
       0.00332226, 0.00498339, 0.00332226, 0.00830565, 0.00996678,
       0.06810631, 0.01162791, 0.00166113, 0.00664452, 0.02159468,
       0.00830565])

def hashfeatures(baby, B, FIX):
    """
    Input:
        baby : a string representing the baby's name to be hashed
        B: the number of dimensions to be in the feature vector
        FIX: the number of chunks to extract and hash from each string
    
    Output:
        v: a feature vector representing the input string
    """
    v = np.zeros(B)
    for m in range(FIX):
        featurestring = "prefix" + baby[:m]
        v[hash(featurestring) % B] = 1
        featurestring = "suffix" + baby[-1*m:]
        v[hash(featurestring) % B] = 1
    return v

def name2features(filename, B=128, FIX=3, LoadFile=True):
    """
    Output:
        X : n feature vectors of dimension B, (nxB)
    """
    # read in baby names
    if LoadFile:
        with open(filename, 'r') as f:
            babynames = [x.rstrip() for x in f.readlines() if len(x) > 0]
    else:
        babynames = filename.split('\n')
    n = len(babynames)
    X = np.zeros((n, B))
    for i in range(n):
        X[i,:] = hashfeatures(babynames[i], B, FIX)
    return X

def naivebayes_pred(pos, neg, posprob, negprob, X_test):
    """
    naivebayes_pred(pos, neg, posprob, negprob, X_test) returns the prediction of each point in X_test
    
    Input:
        pos: class probability for the negative class
        neg: class probability for the positive class
        posprob: conditional probabilities for the positive class (d)
        negprob: conditional probabilities for the negative class (d)
        X_test : features (nxd)
    
    Output:
        prediction of each point in X_test (n)
    """
    n, d = X_test.shape
    
    preds = np.zeros(n)
    
    Theta_1_pos_1 = posprob.copy()
    Theta_0_pos_1 = np.ones(d)-Theta_1_pos_1
    
    Theta_1_neg_1 = negprob.copy()
    Theta_0_neg_1 = np.ones(d)-Theta_1_neg_1
    
    
    Theta_1_pos_1 = np.log(Theta_1_pos_1)
    Theta_0_pos_1 = np.log(Theta_0_pos_1)
    
    Theta_0_neg_1 = np.log(Theta_0_neg_1)
    Theta_1_neg_1 = np.log(Theta_1_neg_1)
    
    log_y_pos = np.log(pos)
    log_y_neg = np.log(neg)
    
    #print(Theta_1_pos_1,Theta_0_pos_1)
    #print(Theta_1_neg_1,Theta_0_neg_1)
    
    for i in range(n):
        xi = X_test[i,:] #xi vector/row
        
        # the log likelihoods of xTestA = 1 + log likelihoods of xTestA = 0 + log likelihood of y=1
        log_pos = np.dot(xi,Theta_1_pos_1) + np.dot((-1*xi+np.ones(d)),Theta_0_pos_1) + log_y_pos
        
        # the log likelihoods of xTestA = 1 + log likelihoods of xTestA = 0 + log likelihood of y=-1
        log_neg = np.dot(xi,Theta_1_neg_1) + np.dot((-1*xi+np.ones(d)),Theta_0_neg_1) + log_y_neg
        #added this print statement in because sometimes this is where math sometimes seems to not work correctly
        #It seems like for some reason when I put this comment here, the math works.  It might be a rounding error
        #I might do the final math somewhere else to ensure it is not rounded off or something.
        print(log_pos,log_neg)
        log_ratio = log_pos - log_neg
        
        if log_ratio > 0:
            preds[i] = 1
        else:
            preds[i] = -1
    
    return preds

def name_classifier(name):
    xtest = name2features(name.capitalize(), B=DIMS, LoadFile=False)
    pred = naivebayes_pred(pos, neg, posprob, negprob, xtest)
    response = {}
    print(pred)
    if pred > 0:
        response["prediction"]= "male"
    else:
        response["prediction"]= "female"

    return response