def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### lazy method 1
    accuracy = clf.score(features_test, labels_test)
    print accuracy

    ### lazy method 2   
    # use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(pred, labels_test)
    print accuracy

    ### method 3
    # compute ratio of well-predicted labels for whole sample

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    
    return accuracy