import nextcord, random, asyncio, dotenv, os
from nextcord.ui import Button, View
from nextcord import Interaction, SlashOption
from nextcord.ext import commands


intents = nextcord.Intents.all()
intents.members = True
command_prefix = '!'

client = commands.Bot(command_prefix, intents = intents)
AUTHKEY= os.environ.get("AirtableKey")
TOKEN= os.environ.get("TOKEN")
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print(command_prefix)

#AIRTABLE

headers = {

    'Authorization': AUTHKEY
}
testserver = 1003826673197781054



#Rock Paper scisors

@client.slash_command(name="rps", description="Rock Paper Scissors, for me info do /rps help")
async def rps(interaction: Interaction, bet:int):
    enemyrps = random.randint(1,3)

    embed1 = nextcord.Embed(title="ROCK PAPER SCISSORS", description="`!rps {bet}`\n **Example:** !rps rock 100\n`{bet} = bet>=0`",
     url="https://en.wikipedia.org/wiki/Rock_paper_scissors", color=0xF5D3F8)
    embed1.set_thumbnail(url="https://arcade.strandedverse.com/static/media/rps-cta.e3f56e8d2357d9d68a67.png")

    embed2 = nextcord.Embed(title="ROCK PAPER SCISSORS", description="Choose one", color=0xF5D3F8)
    embed2.set_thumbnail(url="https://arcade.strandedverse.com/static/media/rps-cta.e3f56e8d2357d9d68a67.png")

    buttonRock = Button(label="Rock", style=nextcord.ButtonStyle.green, emoji="🗿")
    buttonPaper = Button(label="Paper", style=nextcord.ButtonStyle.green, emoji="🤚")
    buttonScissors = Button(label="Scissors", style=nextcord.ButtonStyle.green, emoji="✂")

    view = View()
    view.add_item(buttonRock)
    view.add_item(buttonPaper)
    view.add_item(buttonScissors)
    msg = await interaction.response.send_message(embed=embed2, view=view, ephemeral=True)

    async def button_callback(interaction):
        if enemyrps == 1:
            await interaction.response.send_message("**You:** Rock :rock:, **Opponent:** Rock :rock:\nIt's a tie!", ephemeral=True)
        elif enemyrps == 2:
            await interaction.response.send_message("**You:** Rock :rock:, **Opponent:** Paper :roll_of_paper:\nYou lost, paper beats rock", ephemeral=True)
        elif enemyrps == 3:
            await interaction.response.send_message("**You:** Rock :rock:, **Opponent:** Scissors :scissors:\nYou win, rock beats scissors", ephemeral=True)
    buttonRock.callback = button_callback

    async def button_callback(interaction):
        if enemyrps == 1:
            await interaction.response.send_message("**You:** Paper :roll_of_paper:, **Opponent:** Rock :rock:\nYou win, paper beats rock", ephemeral=True)
        elif enemyrps == 2:
            await interaction.response.send_message("**You:** Paper :roll_of_paper:, **Opponent:** Paper :roll_of_paper:\nIt's a tie!", ephemeral=True)
        elif enemyrps == 3:
            await interaction.response.send_message("**You:** Paper :roll_of_paper:, **Opponent:** Scissors :scissors:\nYou lose, scissors beat paper", ephemeral=True)
    buttonPaper.callback = button_callback

    async def button_callback(interaction):
        if enemyrps == 1:
            await interaction.response.send_message("**You:** scissors :scissors:, **Opponent:** Rock :rock:\nYou lose, rock beats scissors", ephemeral=True)
        elif enemyrps == 2:
            await interaction.response.send_message("**You:** Scissors :scissors:, **Opponent:** Paper :roll_of_paper: \nYou win, scissors beat paper", ephemeral=True)
        elif enemyrps == 3:
            await interaction.response.send_message("**You:** Scissors :scissors:, **Opponent:** Scissors :scissors:\nIt's a tie!", ephemeral=True)
    buttonScissors.callback = button_callback


#WIRES 

@client.slash_command(name = "wires", description = "Wires arcade game")
async def wires(interaction: Interaction, bet:int):
    win =  [["A1","A2","A3"],["A1","B2","B3"],["A1","A2","B3"],["A1","B2","A3"],["B1","B2","B3"],["B1","A2","A3"],["B1","B2","A3"],["B1","A2","B3"]]
   





#Roulete button
@client.slash_command(name="spin", description="Spinner")
async def spin(interaction: Interaction, bet:int = SlashOption(description="Input the ammount you want to bet, bet > 0", required=False)):

        spin1= random.randint(1,6)
        
        global used
        await asyncio.sleep(2)
        used=False
        #button design   
        embed1 = nextcord.Embed(title="Spinner", description="`!spin {bet}`\n **Example:** !spin 100\n`{bet} = bet>=0`", url="https://en.wikipedia.org/wiki/Roulette", color=0xF5D3F8)
        embed1.set_thumbnail(url="https://arcade.strandedverse.com/static/media/spinner.51394a7c48dc8b8f8c52.jpg")
        embed2 = nextcord.Embed(title="Spinner", description="Choose one", color=0xF5D3F8)
        embed2.set_thumbnail(url="https://arcade.strandedverse.com/static/media/spinner.51394a7c48dc8b8f8c52.jpg")
        # ax="6x"
        # ux="3x"
        # ix="2x"

#asking the value of x
        embed2 = nextcord.Embed(title="Spinner", description="Choose one", color=0xF5D3F8)
        embed2.set_thumbnail(url="https://arcade.strandedverse.com/static/media/spinner.51394a7c48dc8b8f8c52.jpg")
        sixx = Button(label="6x", style=nextcord.ButtonStyle.green)
        threex = Button(label="3x", style=nextcord.ButtonStyle.green)
        twox = Button(label="2x", style=nextcord.ButtonStyle.green)

        view = View()
        view.add_item(sixx)
        view.add_item(threex)
        view.add_item(twox)
        await interaction.response.send_message(embed=embed2, view=view, ephemeral=True)


        async def button_callback(interaction):
            print("6x answer", spin1) 
            global Mercl
            global Scrapl
            global Buildl
            global Propl
            global Warl
            global Anarl
            Mercl=Button(label="Mercenaries", style=nextcord.ButtonStyle.green, emoji="<:merc:1005890977174667394>")
            Scrapl = Button(label="Scrappers", style=nextcord.ButtonStyle.green, emoji="<:scrapper:1005891477701923006>")
            Buildl = Button(label="Builders", style=nextcord.ButtonStyle.green, emoji="<:builder:1005891474371649566>")
            Propl = Button(label="Prophets", style=nextcord.ButtonStyle.green, emoji="<:prophet:1005891475827073145>")
            Warl = Button(label="Warlords", style=nextcord.ButtonStyle.green, emoji="<:warlord:1005891479090245662>")
            Anarl = Button(label="Anarchists", style=nextcord.ButtonStyle.green, emoji="<:anarchist:1005891472840720554>")
            merc='https://cdn.discordapp.com/attachments/1003826673197781054/1004444807579574392/merc.gif'
            scrap='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519448772749/scrap.gif'
            builder='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519851430058/builders.gif'
            prop='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520321196093/prop.gif'
            warlords ='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520673501304/war.gif'
            anar='https://cdn.discordapp.com/attachments/1004424185864540180/1004447521038401626/anar.gif'
            view = View()
            view.add_item(Mercl)
            view.add_item(Scrapl)
            view.add_item(Buildl)    
            view.add_item(Propl)
            view.add_item(Warl)
            view.add_item(Anarl)
            await interaction.response.send_message(embed=embed2, view=view, ephemeral=True)
        
            #gif assign
            
            global winning
            global gif
            gif=0
            winning="Error"
            if spin1==1:
                gif=(merc)
                winning="Mercenaries"
            elif spin1==2:
                gif=(scrap)
                winning="Scrappers"
            elif spin1==3:
                gif=(builder)
                winning="Builders"
            elif spin1==4:
                gif=(prop)
                winning="Prophets"
            elif spin1==5:
                gif=(warlords)
                winning="Warlords"
            elif spin1==6:
                gif=(anar)
                winning="Anarchists"
            else:
                print("dude gif thingy is not working")

            async def button_callback(interaction):
                global winning
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)

                    await asyncio.sleep(2)
                    if spin1==1:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Mercenaries** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Mercl.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==2:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Scrappers** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Scrapl.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==3:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Builders** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Buildl.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==4:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Prophets** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Propl.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==5:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Warlords** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Warl.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==6:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Anarchists** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            Anarl.callback = button_callback
        sixx.callback = button_callback



        async def button_callback(interaction):
            print("3x answer", spin1) 
            embed2 = nextcord.Embed(title="Spinner", description="Choose one", color=0xF5D3F8)
            embed2.set_thumbnail(url="https://arcade.strandedverse.com/static/media/spinner.51394a7c48dc8b8f8c52.jpg")
            ms = Button(label="Mercenaries And Scrappers\n", style=nextcord.ButtonStyle.green, emoji="<:mm:1006193355530702920>")
            sb = Button(label="Scrappers And Builders\n", style=nextcord.ButtonStyle.green, emoji="<:sb:1006194818491367615>")
            bp = Button(label="Builders And Prophets\n", style=nextcord.ButtonStyle.green, emoji="<:bp:1006194804306219072>")
            pw = Button(label="Prophets and Warlords\n", style=nextcord.ButtonStyle.green, emoji="<:pw:1006194812912939039>")
            wa = Button(label="Warlords And Anarchists\n", style=nextcord.ButtonStyle.green, emoji="<:wa:1006194821905526844>")
            am = Button(label="Anarchists And Mercenaries\n", style=nextcord.ButtonStyle.green, emoji="<:am:1006194801244377090>")
#  :anarchist: :builder: :merc: :prophet: :scrapper: :warlord: 
            view = View()
            view.add_item(ms)
            view.add_item(sb)
            view.add_item(bp)
            view.add_item(pw)
            view.add_item(wa)
            view.add_item(am)
            await interaction.response.send_message(embed=embed2, view=view, ephemeral=True)
            global winning
            global gif
            merc2='https://cdn.discordapp.com/attachments/1003826673197781054/1004444807579574392/merc.gif'
            scrap2='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519448772749/scrap.gif'
            builder2='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519851430058/builders.gif'
            prop2='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520321196093/prop.gif'
            warlords2 ='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520673501304/war.gif'
            anar2='https://cdn.discordapp.com/attachments/1004424185864540180/1004447521038401626/anar.gif'
            gif='heyy'
            winning="Error"
            tt=random.randint(1,2)
            if spin1==1:
                if tt==1:
                    gif=(merc2)
                else:
                    gif=(scrap2)
                winning="Mercenaries And Scrappers"
            elif spin1==2:
                if tt==1:
                    gif=(scrap2)
                else:
                    gif=(builder2)
                winning="Scrappers And Builders"
            elif spin1==3:
                if tt==1:
                    gif=(builder2)
                else:
                    gif=(prop2)
                winning="Builders And Prophets"
            elif spin1==4:
                if tt==1:
                    gif=(prop2)
                else:
                    gif=(warlords2)
                winning="Prophets And Warlords"
            elif spin1==5:
                if tt==1:
                    gif=(warlords2)
                else:
                    gif=(anar2)
                winning="Warlords And Anarchists"
            elif spin1==6:
                if tt==1:
                    gif=(anar2)
                else:
                    gif=(merc2)
                winning="Anarchists And Mercenaries"
            else:
                print("dude gif thingy is not working")

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                global winning
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==1:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Mercenaries And Scrappers** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            ms.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==2:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Scrappers And Builders** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            sb.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==3:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Builders And Prophets** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            bp.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==4:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Prophets And Warlords** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            pw.callback = button_callback

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==5:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Warlords And Anarchists** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            wa.callback = button_callback
            
            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin1==6:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Anarchists And Mercenaries** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            am.callback = button_callback
        threex.callback = button_callback



        async def button_callback(interaction):
            embed2 = nextcord.Embed(title="Spinner", description="Choose one", color=0xF5D3F8)
            embed2.set_thumbnail(url="https://arcade.strandedverse.com/static/media/spinner.51394a7c48dc8b8f8c52.jpg")
            fq = Button(label="Mercenaries, Scrappers And Builders\n", style=nextcord.ButtonStyle.green, emoji="<:fq:1006476121778430013>")
            sq = Button(label="Prophets, Warlords And Anarchists\n", style=nextcord.ButtonStyle.green, emoji="<:sq:1006476124953522176>")

#  :anarchist: :builder: :merc: :prophet: :scrapper: :warlord: 
            view = View()
            view.add_item(fq)
            view.add_item(sq)
            await interaction.response.send_message(embed=embed2, view=view, ephemeral=True)
            global winning
            global gif
            merc3='https://cdn.discordapp.com/attachments/1003826673197781054/1004444807579574392/merc.gif'
            scrap3='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519448772749/scrap.gif'
            builder3='https://cdn.discordapp.com/attachments/1004424185864540180/1004447519851430058/builders.gif'
            prop3='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520321196093/prop.gif'
            warlords3 ='https://cdn.discordapp.com/attachments/1004424185864540180/1004447520673501304/war.gif'
            anar3='https://cdn.discordapp.com/attachments/1004424185864540180/1004447521038401626/anar.gif'
            spin3=random.randint(1,2)
            print("2x answer for", spin3) 
            gif='heyy'
            winning="Error"
            tt=random.randint(1,3)
            if spin3==1:
                if tt==1:
                    gif=(merc3)
                elif tt==2:
                    gif=(scrap3)
                else:
                    gif=(builder3)
                winning="Mercenaries, Scrappers And Builders"
            elif spin3==2:
                if tt==1:
                    gif=(prop3)
                elif tt==2:
                    gif=(warlords3)
                else:
                    gif=(anar3)
                winning="Prophets, Warlords And Anarchists"
            else:
                print("dude gif thingy is not working")

            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                global winning
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin3==1:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Mercenaries, Scrappers And Builders** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            fq.callback = button_callback
            async def button_callback(interaction):
                global used
                await asyncio.sleep(2)
                global winning
                if used==False:
                    await interaction.response.edit_message(content=gif, embed=None, view=None)
                    if spin3==2:
                        await interaction.send("Congratulations You Won By Guessing "+"**"+winning+"**", ephemeral=True)
                    else:
                        await interaction.send("Unfortunatelly You Guessed **Prophets, Warlords And Anarchists** But The Answer is "+"**"+winning+"**",ephemeral=True)
                else:
                    print("We got cheater guys")
                used=True
            sq.callback = button_callback
        twox.callback = button_callback  
@client.command(name="hey")
async def hey(ctx):
    await ctx.reply("hi")
client.run(TOKEN)
