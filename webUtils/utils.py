class Generic:
    def windowHandler(self):
        handles= driver.window_handles
        current= driver.current_window_handles
        for item in handles:
            driver.switch_to.window(item)
            if item!=current:
                break