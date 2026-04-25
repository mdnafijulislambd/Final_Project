# class TestData:
#     BASE_URL = "https://labsqajobs.qaharbor.com/"
#     EXISTING_EMAIL = "qqq@gmail.com"
#     PASSWORD = "11111111"
#     EXISTING_EMAIL_1 = "ooo@gmail.com"
#     PASSWORD_1 = "000000000000"



# import time


# class TestData:
#     BASE_URL = "https://labsqajobs.qaharbor.com/"

#     # ✅ existing user (login / duplicate test)
#     EXISTING_EMAIL = "qqq@gmail.com"
#     PASSWORD = "11111111"

#     EXISTING_EMAIL_1 = "ooo@gmail.com"
#     PASSWORD_1 = "000000000000"

#     # ✅ dynamic generator (NEW)
#     @staticmethod
#     def generate_candidate():
#         ts = int(time.time())
#         return {
#             "username": f"user{ts}",
#             "email": f"user{ts}@gmail.com",
#             "password": "12345678"
#         }

#     @staticmethod
#     def generate_recruiter():
#         ts = int(time.time())
#         return {
#             "company": f"Company{ts}",
#             "email": f"recruiter{ts}@gmail.com",
#             "phone": f"017{ts}"[-11:],
#             "password": "12345678"
#         }



import time


class TestData:
    BASE_URL = "https://labsqajobs.qaharbor.com/"

    # =========================
    # EXISTING USERS (STATIC)
    # =========================
    EXISTING_EMAIL = "qqq@gmail.com"
    PASSWORD = "11111111"

    EXISTING_EMAIL_1 = "ooo@gmail.com"
    PASSWORD_1 = "000000000000"

    # =========================
    # VALID CANDIDATE (DYNAMIC)
    # =========================
    @staticmethod
    def generate_candidate():
        ts = int(time.time())
        return {
            "username": f"user_{ts}",
            "email": f"user_{ts}@gmail.com",
            "password": "12345678"
        }

    # =========================
    # VALID RECRUITER (DYNAMIC)
    # =========================
    @staticmethod
    def generate_recruiter():
        ts = int(time.time())
        return {
            "company": f"Company{ts}",
            "email": f"recruiter{ts}@gmail.com",
            "phone": f"017{ts}"[-11:],
            "password": "12345678"
        }

    # =========================
    # INVALID DATA (NEGATIVE TEST)
    # =========================
    @staticmethod
    def generate_invalid_email():
        ts = int(time.time())
        return f"user_{ts}@gmal.con"

    @staticmethod
    def generate_invalid_user():
        ts = int(time.time())
        return {
            "username": f"user_{ts}",
            "email": f"user_{ts}@gmal.con",
            "password": "12345678"
        }