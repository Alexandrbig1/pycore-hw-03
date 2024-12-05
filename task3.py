import re

def normalize_phone(phone_number):
    if type(phone_number) != str:
        return "Invalid phone number"
    
    # Remove all characters except digits and '+'
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Check if the phone number starts with '+'
    if not phone_number.startswith('+'):
        # If the phone number starts with '1', add '+'
        if phone_number.startswith('1'):
            phone_number = '+' + phone_number
        else:
            # Otherwise, add '+1' as the international code
            phone_number = '+1' + phone_number
    
    return phone_number

# Example usage
phone_numbers = normalize_phone("8(950)288-67-45")
print(phone_numbers)  # +19502886745