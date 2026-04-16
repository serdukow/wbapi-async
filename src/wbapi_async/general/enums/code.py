from enum import StrEnum


class Code(StrEnum):
    """The code for the seller account section the user will get access to:"""

    BALANCE = "balance"
    BRANDS = "brands"
    CHANGEJAM = "changeJam"
    DISCOUNTPRICE = "discountPrice"
    FINANCE = "finance"
    SHOWCASE = "showcase"
    SUPPLIERSDOCUMENTS = "suppliersDocuments"
    SUPPLY = "supply"
    FEEDBACKSQUESTIONS = "feedbacksQuestions"
    QUESTIONS = "questions"
    PINFEEDBACKS = "pinFeedbacks"
    POINTSFORREVIEWS = "pointsForReviews"
    FEEDBACKS = "feedbacks"
    WBPOINT = "wbPoint"
