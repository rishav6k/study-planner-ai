import json

def handler(event, context):
    try:
        body = json.loads(event["body"])

        subject = body.get("subject", "")
        hours = body.get("hours", 0)
        days = body.get("days", 0)
        missed_days = body.get("missed_days", 0)

        if not subject:
            return {"statusCode": 400, "body": "Subject required"}

        remaining_days = days - missed_days
        if remaining_days <= 0:
            return {"statusCode": 400, "body": "Invalid days"}

        hours_per_day = round(hours / remaining_days, 2)

        plan = f"Study {subject} {hours_per_day} hrs daily for {remaining_days} days"

        return {
            "statusCode": 200,
            "body": json.dumps({
                "plan": plan
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
