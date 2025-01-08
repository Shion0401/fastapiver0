import sys
import api.models.models as models
import api.db as databases

import datetime

sys.dont_write_bytecode = True


## GetReport
async def GetReport(user_id):
    session = databases.create_new_session()
    report = session.query(models.Report).\
                filter(models.Report.user_id == user_id).\
                first()         
    if report == None:
        return 'None'
    return report.times


## InsertReport
async def InsertReport(user_id):
    session = databases.create_new_session()
    report = models.Report()
    report.times = 1
    report.update_date_time = datetime.datetime.now()
    report.user_id = user_id
    session.add(report)
    session.commit()
    return report.times
    
    
## UpdateReport
async def UpdateReport(user_id):
    session = databases.create_new_session()
    report = session.query(models.Report).\
                filter(models.Report.user_id == user_id).\
                first()
    if report == None:
        return -1
    report.times += 1
    report.update_date_time = datetime.datetime.now()
    session.commit()
    return report.times

    
## DeleteReport
def DeleteReport(user_id):
    session = databases.create_new_session()
    report = session.query(models.Report).\
                filter(models.Report.user_id == user_id).\
                first()
    if report == None:
        return -1
    session.delete(report)
    session.commit()
    return 0
    
