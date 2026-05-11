OK_FORMAT = True

test = {   'name': 'q5',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> assert np.isclose(lasso_cv.alpha_, 0.0016, atol=0.0001)\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert len(lasso_cv.coef_) == 8\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
