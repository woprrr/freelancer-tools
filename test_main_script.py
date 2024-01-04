import unittest
from unittest.mock import patch, call
import main_script
from config import Messages

class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['500', '5', 'oui', '4'])
    @patch('builtins.print')
    def test_main_yes_option(self, mock_print, mock_input):
        main_script.main()
        expected_calls = [
            call(Messages.MONTHLY_INCOME.format('10000.0')),
            call(Messages.ADJUST_MODIFY_DAYS),
            call(Messages.NEW_DAR.format(4, '625.0'))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['500', '5', 'non'])
    @patch('builtins.print')
    def test_main_no_option(self, mock_print, mock_input):
        main_script.main()
        expected_calls = [
            call(Messages.MONTHLY_INCOME.format('10000.0')),
            call(Messages.ADJUST_MODIFY_DAYS),
            call(Messages.NO_MODIFICATION)
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['500', '5', 'oui', 'non'])
    @patch('builtins.print')
    def test_invalid_input_for_modify_days(self, mock_print, mock_input):
        with self.assertRaises(ValueError):
            main_script.main()

if __name__ == '__main__':
    unittest.main()
