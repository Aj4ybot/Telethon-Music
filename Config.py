import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15239462"))
    API_HASH = os.environ.get("API_HASH", "f32586aee67d042cd3c519028f2c3987")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5599833586:AAE-QSiNyw5i34MTUg3sinuz8Pcd5uZt0mo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKsBuyjZ4E43Zqd8Bpvkr_i_jn2fahDq61mTv7KDdOplfuAxfNBpvMccsb7cdczOfTng-VpfxkKwBa019WlaOG4z5v_FAnD3HCHt_ajxGxPQVKPxXscqc1t3_NuJOLtX7qZFF9suct92XBNarhzkbZLjijoTOrr_2m5vSjtybexCfaWv1DZs0gtM7XpoYst5khiCon1U87Vyc4tWu_dEstyuAVtiD5xxZYF4F1w90mvvwNg5SMUcbx1uTAUBfGuLx_6ICS65fAykdXD40JypETYGqmBPLEgKBh0INBMvNmridzq1R-gmEBBRHgI6PMUdYCfwis8DRIsnh11TBfIzrXq7g8E=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
