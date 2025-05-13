from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer


class ReminderCreateAPIView(APIView):
    def post(self, request):
        """
        To Create a new reminder.

        ## Accepts:
        - message: The reminder message to be sent.
        - remind_at: The datetime at which the reminder should be triggered (ISO 8601 format).
        - remind_via: Method of sending the reminder ("email" or "sms").

        ## Returns:
        - 201 Created with reminder details on success.
        - 400 Bad Request with error messages on failure.

        ## Request Body
            {
                "message": "Attend the meeting",
                "remind_at": "2025-05-12T17:30:00Z",
                "remind_via": "email"
            }

        ## Response Body:
            {
                "id": 1,
                "message": "Attend the meeting",
                "remind_at": "2025-05-12T17:30:00Z",
                "remind_via": "email"
            }
        """
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
