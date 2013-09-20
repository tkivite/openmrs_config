{
	'name' : 'eHospital OpenMRS Configuration module',
	'version' : '0.1',
	'author' : 'Titus Kivite @ Intellisoft',
	'website' : 'http://www.intellisoftkenya.com/',
	'category' : 'Generic Modules/Others',
	'depends' : ['base'],
	'description' : 'This module configures the properties required for openmrs integration',
	'demo_xml' : [],
	'data' : ['security/security.xml','openmrs_config.xml', 'data/config_data.xml', 'security/ir.model.access.csv',],
	'active': False,
	'installable': True,
}
