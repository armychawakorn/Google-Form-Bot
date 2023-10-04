import Chawakorn #เรียกใช้งานไลบรารี Chawakorn

#ตั้งค่าbot=============================================================================================
bot = Chawakorn.Bot('https://docs.google.com/forms/d/e/1FAIpQLScbfRP37Bl8As_2DB_geT1o_jPUu6LMe-z37Nk4BgwEMFtWAw/viewform?usp=sf_link')
#bot = Chawakorn.Bot('urlของฟอร์ม')
#====================================================================================================


for i in range(10): #ทำซ้ำ 10 ครั้ง
    #บอกให้้บอทเริ่มทำงาน=======
    bot.Start()
    #=======================

    #สั่งให้บอทกรอกข้อมูลในฟอร์ม===========================
    bot.send_Fill_Form('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 'Chawakorn')
    #bot.send_Fill_Form(xpath, ข้อความที่จะให้กรอก)
    #=================================================
    
    #สั่งให้บอทคลิกปุ่ม================================
    bot.send_Click('//*[@id="i9"]/div[3]/div')
    #bot.send_Click(xpath)
    #=============================================

    #สั่งให้บอทเลือกตัวเลือกสุ่ม 1===========================
    bot.send_Random_Fill_Form([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[4]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[5]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[6]/div/div/div[3]/div'
    ])
    #bot.send_Random_Fill_Form([xpath1, xpath2, xpath3, xpath4, xpath5])
    #=================================================
    
    #สั่งให้บอทเลือกตัวเลือกสุ่ม 2===========================
    bot.send_Random_Fill_Form([
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[4]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[5]/div/div/div[3]/div',
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[6]/div/div/div[3]/div'
    ])
    #bot.send_Random_Fill_Form([xpath1, xpath2, xpath3, xpath4, xpath5])
    #=================================================

    #สั่งให้บอทคลิกปุ่ม================================
    bot.send_Click('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    #bot.send_Click(xpath)
    #=============================================
    
    #บอกให้บอทหยุดทำงาน==============
    bot.close()
    #===============================
    
    print(f'สำเร็จครั้งที่ {i+1}')