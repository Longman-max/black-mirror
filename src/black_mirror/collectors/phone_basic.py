from typing import Dict, Any
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from black_mirror.collectors import Collector

class PhoneBasicCollector(Collector):
    @property
    def name(self) -> str:
        return "phone_basic"

    @property
    def supported_types(self) -> list[str]:
        return ["phone"]

    def run(self, query: str) -> Dict[str, Any]:
        try:
            # Parse the number
            # We assume the query might be in international format, but if not, we can't guess region easily without more info.
            # However, for OSINT, we usually expect +CountryCode.
            parsed_number = phonenumbers.parse(query, None)
            
            is_valid = phonenumbers.is_valid_number(parsed_number)
            is_possible = phonenumbers.is_possible_number(parsed_number)
            
            region_code = phonenumbers.region_code_for_number(parsed_number)
            country_name = geocoder.description_for_number(parsed_number, "en")
            carrier_name = carrier.name_for_number(parsed_number, "en")
            time_zones = timezone.time_zones_for_number(parsed_number)

            return {
                "valid": is_valid,
                "possible": is_possible,
                "formatted_e164": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
                "formatted_international": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "region_code": region_code,
                "country": country_name,
                "carrier": carrier_name,
                "timezones": list(time_zones)
            }
        except phonenumbers.NumberParseException as e:
            return {
                "valid": False,
                "error": str(e)
            }
