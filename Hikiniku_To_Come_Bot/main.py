### Main script to run the booking process

from datetime import datetime
import undetected_chromedriver as uc
from booking import Booking


def _IsValidTimeSlot(time_slot:str) -> bool:

    if not isinstance(time_slot, list):
        raise TypeError("Please input a list")

    time_format = "%H-%M"

    for time in TimeSlot:
        time_fstr = datetime.strptime(time, time_format)
        StartTime = datetime.strptime("11-00", time_format)
        EndTime = datetime.strptime("21-15", time_format)

        if not StartTime <= time_fstr <= EndTime:
            raise Exception(f"Time Slot: {time_fstr.strftime('%H-%M')} exceed the range 11:00 - 21:15")

    return True


def main(
    options_list:list,
    keep_alive:bool = False,
    party_size: int = 2,
    time_slot:list = []
):

    assert 0 < party_size < 5, "Party Size exceed the range 1 - 4"
    assert _IsValidTimeSlot(time_slot), "Invalid time slot"
    
    url = "https://inline.app/booking/-NxpjjSJhxwTw6cV0Lm3:inline-live-3/-Nxpjjmuxwpudr9s2kHN"

    options = uc.ChromeOptions()
    if options_list:
        for setting in options_list:
            options.add_argument(setting)
    
    ### KeepAlive: Determine if the browser keep or not after run the script.
    driver = uc.Chrome(options=options,
                       enable_cdp_events=keep_alive)
    driver.get(url)

    bot = Booking(driver)
    bot.select_partysize(party_size)

    # date_xpath = f"//div[@data-cy='bt-cal-day' and @data-date='2024-10-13']"
    bot.select_date()



if __name__ == "__main__":

    PartySize = 1
    TimeSlot = ["21-15"]

    options_list = ["--disable-gpu",
                    "--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"]

    main(options_list, True, PartySize, TimeSlot)