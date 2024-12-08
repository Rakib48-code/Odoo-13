{
    'name': 'My First Module',
    'category': 'Uncategory',
    'summary': 'Create My First Module',
    'sequence': '-100',
    'version': '0.1.2.2',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view_school_menu.xml',
        'views/view_student_menu.xml',
        'views/view_course_menu.xml',
        'demo/demo.xml',
        'demo/course_demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
