from tvg.uti import *
adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = load_data()
print('adj:',adj.shape)
print(adj)
print('features:',features.shape)
print(features)
print('y_train:',y_train.shape)
print(y_train)
print('y_test:',y_test.shape)
print(y_test)
print('y_val:',y_val.shape)
print(y_val)
print('train_mask:',train_mask.shape)
print(train_mask)
print('test_mask:',test_mask.shape)
print(test_mask)
print('val_mask:',val_mask.shape)
print(val_mask)