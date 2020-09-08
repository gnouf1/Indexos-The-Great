import discord
import validators as val
import DB.manageDB as mdb
from discord.ext import commands
from discord.ext.commands import bot
from os import remove as rm

PREFIX = open("core/prefix.txt", "r").read().replace("\n", "")


class BaseCommands(commands.Cog):
    def __init__(self, ctx):
        return(None)

    # @commands.command(pass_context=True)
    # async def Ldel(self, ctx, link):
    #     if mdb.deleteLink(link, ctx.author.id):
    #         await ctx.channel.send("Lien supprimé")
    #         await ctx.message.delete()
    #     else:
    #         await ctx.channel.send("Le lien n'a pas pu être supprimé")
    #
    # @commands.command(pass_context=True)
    # async def syndel(self, ctx, oldSyn):
    #     if mdb.deleteSyn(oldSyn, ctx.author.id):
    #         await ctx.channel.send("Synonyme supprimé")
    #         await ctx.message.delete()
    #     else:
    #         await ctx.channel.send("Le synonyme n'a pas pu être supprimé")
    #
    # @commands.command(pass_context=True)
    # async def Lsearch(self, ctx, *tags):
    #     i = 0
    #     for tag in tags:
    #         tag = tag.lower()
    #     reslist = list(mdb.search(tags))
    #     print(reslist)
    #     if reslist:
    #         str = "Liens correspondants à votre recherche :\n"
    #         for elem in reslist:
    #             elemn_tag1 = elem[3]
    #             elemn_tag2 = elem[4]
    #             elemn_tag3 = elem[5]
    #             str += "  **>** "+elem[0]+" ["
    #             if elemn_tag1 is not None:
    #                 if elemn_tag1 in tags:
    #                     strTag = "**" + elemn_tag1 + "**"
    #                 else:
    #                     strTag = elemn_tag1
    #                 str += strTag
    #             if elemn_tag2 is not None:
    #                 if elemn_tag2 in tags:
    #                     strTag = "**" + elemn_tag2 + "**"
    #                 else:
    #                     strTag = elemn_tag2
    #                 str += ", "+strTag
    #             if elemn_tag3 is not None:
    #                 if elemn_tag3 in tags:
    #                     strTag = "**" + elemn_tag3 + "**"
    #                 else:
    #                     strTag = elemn_tag3
    #                 str += ", "+strTag
    #             str += "]\n"
    #             if i % 10 == 0 and i != 0:
    #                 await ctx.channel.send(str)
    #                 str = ""
    #
    #             i += 1
    #
    #     else:
    #         str = "Aucun lien ne correspond à votre recherche"
    #     await ctx.channel.send(str)
    #
    # @commands.command(pass_context=True)
    # async def github(self, ctx):
    #     await ctx.channel.send("https://github.com/gnouf1/Indexos-The-Great")
    #
    # @commands.command(pass_context=True)
    # async def toptag(self, ctx, nb=10):
    #     tag1List = mdb.occurenceInField("tag1")
    #     tag2List = mdb.occurenceInField("tag2")
    #     tag3List = mdb.occurenceInField("tag3")
    #
    #     res = dict()
    #
    # # Va ecrire dans res l'ensemble des tags et l'ensemble de leur occurences
    #     for item in tag1List:
    #         try:
    #             res[item[0]] += item[1]
    #         except KeyError:
    #             res[item[0]] = item[1]
    #
    #     for item in tag2List:
    #         try:
    #             res[item[0]] += item[1]
    #         except KeyError:
    #             res[item[0]] = item[1]
    #
    #     for item in tag3List:
    #         try:
    #             res[item[0]] += item[1]
    #         except KeyError:
    #             res[item[0]] = item[1]
    #
    #     del(res[None])
    #     if nb > len(res) or nb == -1:
    #         nb = len(res)
    #
    #     msg = "**Les {} tags les plus utilisés sont :**\n".format(str(nb))
    #
    #     # Reverse car il classe en croissant.
    #     # res devient une liste
    #     res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    #
    #     # Mesure anti flood
    #     if nb <= 10:
    #         for i in range(0, nb):
    #             msg += "**{}.** {} ({})\n".format(str(i+1), res[i][0], res[i][1])
    #
    #         await ctx.channel.send(msg)
    #     else:
    #         for i in range(0, nb):
    #             msg += "**{}.** {} ({})\n".format(str(i+1), res[i][0], res[i][1])
    #             if i % 50 == 0 and i != 0:
    #                 await ctx.author.send(msg)
    #                 msg = ""
    #         await ctx.author.send(msg)
    #
    # @commands.command(pass_context=True)
    # async def DBdump(self, ctx):
    #     await ctx.author.send("Création du fichier...")
    #     fp = mdb.dumpAllDB()
    #     fileD = discord.File(fp, "dump_file.sql")
    #     await ctx.author.send(file=fileD)
    #     rm(fp)
    #     await ctx.channel.send("Fichier envoyé")
    #
    #
    # @commands.command(pass_context=True)
    # async def merge(self, ctx, old, new):
    #     authID = ctx.author.id
    #     if len(mdb.searchByTag(old)) != 0 and len(mdb.searchByTag(new)) != 0:
    #         mdb.changetags(old, new)
    #         await ctx.channel.send("Les tags *{}* ont été fusionné avec *{}*".format(old, new))
    #         mdb.createSynonyme(authID, old, new)
    #     else:
    #         await ctx.channel.send("Les tags que vous essayez de fusionner n'existe pas.")
    #
    #
    # @commands.command(pass_context=True)
    # async def synlist(self, ctx):
    #     liste = mdb.allSynonyme()
    #     msg = ""
    #     i = 0
    #     if liste:
    #         msg = "**Les synonymes suivant sont enregistrés :** \n"
    #         for elem in liste:
    #             i += 1
    #             msg += "    *{0}* -> {1} \n".format(elem[1], elem[2])
    #             if i % 50 == 0 and i != 0:
    #                 await ctx.channel.send(msg)
    #                 msg = ""
    #     else:
    #         msg = "Rien à afficher"
    #     await ctx.channel.send(msg)

def setup(bot):
    bot.add_cog(BaseCommands(bot))
    open("help/cogs.txt", "a").write("BaseCommands\n")