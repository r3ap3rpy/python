"""
FOC080203H8 - 2004 January

LLLYYWWSSSS

'YY' is the year of manufacture
‘WW’ is the week of manufacture.
 The date code can be found in the 4 middle digits of the serial number.  In the case of serial number SAD08300D4W, ‘08’ is the year code and ‘30’ is the week code.
"""
class SerialConverter(object):
	@classmethod
	def Convert(self, Serial):
		if len(Serial) > 19:
			print('This cannot be converted: {}'.format(Serial))
			return None
		try:
			YearOfManufacturing = 1996 + int(Serial[3:5])
		except:
			print('I could not extract the year of manufacturing form: {}'.format(Serial))
			return None
		try:
			MonthOfManufacturing = int(Serial[5:7])
		except:
			print('I could not extract the month of manufacturing form: {}'.format(Serial))
			return None

		if MonthOfManufacturing in range(1,6):
			MonthOfManufacturing = 'January'
		elif MonthOfManufacturing in range(6,10):
			MonthOfManufacturing = 'February'
		elif MonthOfManufacturing in range(10,15):
			MonthOfManufacturing = 'March'
		elif MonthOfManufacturing in range(15,19):
			MonthOfManufacturing = 'April'
		elif MonthOfManufacturing in range(19,23):
			MonthOfManufacturing = 'May'
		elif MonthOfManufacturing in range(23,28):
			MonthOfManufacturing = 'June'
		elif MonthOfManufacturing in range(28,32):
			MonthOfManufacturing = 'July'
		elif MonthOfManufacturing in range(32,36):
			MonthOfManufacturing = 'August'
		elif MonthOfManufacturing in range(36,41):
			MonthOfManufacturing = 'September'
		elif MonthOfManufacturing in range(41,45):
			MonthOfManufacturing = 'October'	
		elif MonthOfManufacturing in range(45,49):
			MonthOfManufacturing = 'November'	
		elif MonthOfManufacturing in range(49,54):
			MonthOfManufacturing = 'December'
		else:
			print('The serial: {} seems to be malformed!'.format(Serial))
			return None
		return {'Year':YearOfManufacturing, 'Month': MonthOfManufacturing}


Converted = SerialConverter.Convert('Foc08203H8')

if Converted is not None:
	print('The year is: {} and the month is: {} when the device was manufactured!'.format(Converted['Year'],Converted['Month']))