from django.db import models
from book.models import Book
from member.models import Member
# Create your models here.


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrowed_book')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"🙎{self.member} ➡️ {self.book.title}📖"