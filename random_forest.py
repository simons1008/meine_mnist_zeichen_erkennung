try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(base_estimator=deprecated, bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha'), max_depth=None, max_features=sqrt, max_leaf_nodes=20, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=7, n_jobs=None, num_outputs=10, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[38] <= 0.5:
            if x[54] <= 1.5:
                if x[35] <= 9.5:
                    if x[21] <= 2.5:
                        return 5, 121.0
                    else:
                        return 3, 149.0
                else:
                    if x[9] <= 1.5:
                        return 1, 112.0
                    else:
                        return 5, 121.0
            else:
                if x[20] <= 7.5:
                    if x[63] <= 0.5:
                        if x[28] <= 3.5:
                            return 6, 134.0
                        else:
                            return 8, 114.0
                    else:
                        return 1, 112.0
                else:
                    if x[43] <= 3.0:
                        return 3, 149.0
                    else:
                        if x[45] <= 8.5:
                            return 2, 118.0
                        else:
                            return 8, 114.0
        else:
            if x[44] <= 7.5:
                if x[28] <= 2.5:
                    return 0, 133.0
                else:
                    if x[30] <= 1.5:
                        if x[51] <= 9.5:
                            if x[25] <= 1.0:
                                return 3, 149.0
                            else:
                                return 5, 121.0
                        else:
                            if x[28] <= 14.5:
                                return 6, 134.0
                            else:
                                return 3, 149.0
                    else:
                        if x[61] <= 3.5:
                            return 5, 121.0
                        else:
                            return 9, 116.0
            else:
                if x[60] <= 8.5:
                    if x[26] <= 12.5:
                        return 7, 120.0
                    else:
                        return 4, 140.0
                else:
                    return 4, 140.0

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[58] <= 4.5:
            if x[33] <= 8.5:
                if x[13] <= 3.5:
                    if x[62] <= 0.5:
                        if x[29] <= 5.5:
                            if x[28] <= 9.5:
                                return 6, 128.0
                            else:
                                return 1, 132.0
                        else:
                            return 4, 116.0
                    else:
                        return 6, 128.0
                else:
                    if x[5] <= 3.5:
                        if x[36] <= 2.0:
                            return 0, 125.0
                        else:
                            return 1, 132.0
                    else:
                        return 8, 130.0
            else:
                return 4, 116.0
        else:
            if x[60] <= 2.5:
                if x[18] <= 12.0:
                    return 7, 126.0
                else:
                    return 5, 107.0
            else:
                if x[26] <= 4.5:
                    if x[62] <= 1.5:
                        if x[43] <= 5.5:
                            return 3, 161.0
                        else:
                            return 2, 123.0
                    else:
                        if x[45] <= 6.5:
                            return 2, 123.0
                        else:
                            return 3, 161.0
                else:
                    if x[6] <= 0.5:
                        if x[28] <= 2.5:
                            return 0, 125.0
                        else:
                            if x[51] <= 7.5:
                                if x[50] <= 10.5:
                                    return 9, 109.0
                                else:
                                    return 8, 130.0
                            else:
                                return 1, 132.0
                    else:
                        if x[22] <= 0.5:
                            return 5, 107.0
                        else:
                            return 8, 130.0

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[43] <= 1.5:
            if x[41] <= 0.5:
                if x[34] <= 1.5:
                    if x[21] <= 15.5:
                        if x[26] <= 9.0:
                            if x[36] <= 0.5:
                                return 9, 127.0
                            else:
                                return 3, 140.0
                        else:
                            return 5, 124.0
                    else:
                        if x[26] <= 1.5:
                            return 3, 140.0
                        else:
                            return 9, 127.0
                else:
                    return 5, 124.0
            else:
                if x[25] <= 1.5:
                    return 3, 140.0
                else:
                    return 0, 118.0
        else:
            if x[46] <= 6.5:
                if x[28] <= 5.5:
                    if x[29] <= 0.5:
                        if x[42] <= 11.5:
                            return 5, 124.0
                        else:
                            return 6, 128.0
                    else:
                        if x[51] <= 11.5:
                            if x[14] <= 4.0:
                                return 4, 117.0
                            else:
                                return 7, 134.0
                        else:
                            if x[18] <= 11.0:
                                return 2, 130.0
                            else:
                                return 0, 118.0
                else:
                    if x[60] <= 2.5:
                        return 7, 134.0
                    else:
                        if x[9] <= 2.5:
                            if x[33] <= 3.5:
                                return 1, 121.0
                            else:
                                return 4, 117.0
                        else:
                            if x[21] <= 12.5:
                                return 2, 130.0
                            else:
                                return 8, 118.0
            else:
                return 6, 128.0

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[28] <= 5.5:
            if x[10] <= 6.5:
                if x[54] <= 1.5:
                    return 4, 141.0
                else:
                    return 6, 135.0
            else:
                if x[13] <= 2.5:
                    return 6, 135.0
                else:
                    if x[42] <= 8.5:
                        return 5, 117.0
                    else:
                        return 0, 135.0
        else:
            if x[10] <= 8.5:
                if x[37] <= 6.5:
                    return 1, 162.0
                else:
                    if x[60] <= 7.5:
                        return 7, 113.0
                    else:
                        if x[13] <= 15.5:
                            return 4, 141.0
                        else:
                            return 1, 162.0
            else:
                if x[45] <= 6.5:
                    if x[60] <= 2.5:
                        return 7, 113.0
                    else:
                        if x[43] <= 3.5:
                            return 9, 133.0
                        else:
                            if x[33] <= 1.5:
                                if x[54] <= 0.5:
                                    return 8, 95.0
                                else:
                                    return 2, 102.0
                            else:
                                return 1, 162.0
                else:
                    if x[36] <= 4.5:
                        return 9, 133.0
                    else:
                        if x[53] <= 0.5:
                            return 7, 113.0
                        else:
                            if x[38] <= 0.5:
                                if x[42] <= 6.5:
                                    return 3, 124.0
                                else:
                                    return 8, 95.0
                            else:
                                if x[18] <= 10.5:
                                    return 3, 124.0
                                else:
                                    return 9, 133.0

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[21] <= 0.5:
            if x[9] <= 0.5:
                if x[27] <= 15.5:
                    if x[50] <= 1.5:
                        return 4, 144.0
                    else:
                        if x[61] <= 4.0:
                            return 4, 144.0
                        else:
                            return 6, 138.0
                else:
                    if x[2] <= 0.5:
                        return 6, 138.0
                    else:
                        return 1, 102.0
            else:
                return 5, 112.0
        else:
            if x[30] <= 1.5:
                if x[2] <= 5.5:
                    if x[27] <= 6.5:
                        if x[60] <= 7.5:
                            return 7, 108.0
                        else:
                            return 2, 122.0
                    else:
                        if x[20] <= 14.5:
                            return 8, 121.0
                        else:
                            return 1, 102.0
                else:
                    if x[35] <= 11.5:
                        if x[43] <= 2.5:
                            return 3, 154.0
                        else:
                            return 2, 122.0
                    else:
                        return 8, 121.0
            else:
                if x[28] <= 0.5:
                    return 0, 140.0
                else:
                    if x[44] <= 8.5:
                        if x[35] <= 11.5:
                            if x[33] <= 2.5:
                                return 9, 116.0
                            else:
                                return 0, 140.0
                        else:
                            return 7, 108.0
                    else:
                        if x[60] <= 8.5:
                            return 7, 108.0
                        else:
                            if x[34] <= 9.5:
                                return 8, 121.0
                            else:
                                return 4, 144.0

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[26] <= 3.5:
            if x[51] <= 11.5:
                if x[61] <= 0.5:
                    return 7, 120.0
                else:
                    if x[45] <= 8.5:
                        return 9, 131.0
                    else:
                        return 3, 148.0
            else:
                if x[61] <= 0.5:
                    return 7, 120.0
                else:
                    if x[19] <= 13.5:
                        return 2, 144.0
                    else:
                        return 1, 151.0
        else:
            if x[61] <= 10.5:
                if x[42] <= 3.5:
                    if x[45] <= 4.5:
                        return 7, 120.0
                    else:
                        if x[3] <= 5.5:
                            return 9, 131.0
                        else:
                            return 5, 96.0
                else:
                    if x[10] <= 9.5:
                        if x[38] <= 0.5:
                            return 1, 151.0
                        else:
                            return 4, 114.0
                    else:
                        if x[28] <= 5.5:
                            if x[29] <= 0.5:
                                return 5, 96.0
                            else:
                                return 0, 111.0
                        else:
                            if x[51] <= 12.5:
                                return 8, 110.0
                            else:
                                if x[60] <= 2.5:
                                    return 7, 120.0
                                else:
                                    return 1, 151.0
            else:
                if x[21] <= 0.5:
                    if x[42] <= 8.0:
                        return 1, 151.0
                    else:
                        return 6, 132.0
                else:
                    if x[50] <= 1.5:
                        return 1, 151.0
                    else:
                        return 9, 131.0

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[26] <= 3.5:
            if x[4] <= 10.5:
                if x[58] <= 5.0:
                    return 1, 125.0
                else:
                    return 2, 110.0
            else:
                if x[51] <= 10.5:
                    if x[34] <= 3.5:
                        return 3, 143.0
                    else:
                        return 7, 123.0
                else:
                    if x[30] <= 0.5:
                        return 2, 110.0
                    else:
                        return 7, 123.0
        else:
            if x[42] <= 3.5:
                if x[29] <= 11.5:
                    if x[21] <= 2.0:
                        if x[62] <= 5.0:
                            return 5, 104.0
                        else:
                            return 1, 125.0
                    else:
                        return 3, 143.0
                else:
                    if x[44] <= 6.5:
                        return 9, 141.0
                    else:
                        return 7, 123.0
            else:
                if x[13] <= 3.5:
                    if x[54] <= 2.5:
                        if x[33] <= 3.5:
                            return 8, 105.0
                        else:
                            return 4, 151.0
                    else:
                        return 6, 126.0
                else:
                    if x[28] <= 2.5:
                        if x[21] <= 0.5:
                            return 5, 104.0
                        else:
                            return 0, 129.0
                    else:
                        if x[51] <= 15.5:
                            if x[50] <= 4.0:
                                if x[58] <= 0.5:
                                    return 4, 151.0
                                else:
                                    return 7, 123.0
                            else:
                                return 8, 105.0
                        else:
                            return 1, 125.0