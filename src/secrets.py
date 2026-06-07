from pydantic import BaseModel, SecretBytes, SecretStr, field_serializer

class Model(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes

    # Dump the real value when serializes as JSON, overriding default behavior which obfuscates the values
    @field_serializer('password', 'password_bytes', when_used='json')
    def dump_secretxxxxxxxxxxx(self, v): # function name does not matter here, but the decorator matters
        return v.get_secret_value()

model = Model(password='IAmSensitive', password_bytes=b'IAmSensitiveBytes')
# print(model)
# #> password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
# print(model.password)
# #> **********
# print(model.model_dump())
"""
{
    'password': SecretStr('**********'),
    'password_bytes': SecretBytes(b'**********'),
}
"""
print(model.model_dump_json())
#> {"password":"IAmSensitive","password_bytes":"IAmSensitiveBytes"}

