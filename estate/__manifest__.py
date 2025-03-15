{
    'name': "Test App",
    'depends': ['base'],
    'application': 'True',
    'description': '''
    This is a test app
    ''',

    '''
    'data' is sequentially loaded, so write down the nondepended files first and then the depended files.
    '''

    'data': [
        'security/ir.model.access.csv',
    ],
    

}
