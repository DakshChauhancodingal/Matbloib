import matplotlib.pyplot as plt
"""
import matplotlib.ticker as ticker
fig,axes=plt.subplots(2,2,figsize=(14,9))
fig.suptitle('Social media trendy dashboard',fontsize=20,fontweight='bold',y=0.98)
fig.patch.set_color("#f8f9fa")
ax1=axes[0,0]
ax2=axes[0,1]
ax3=axes[1,0]
ax4=axes[1,1]
plt.tight_layout()
plt.show()"""
days=["Mon","Tue","wed","Thu","Fri","Sat","Sun"]
instagram=[12,15,14,16,19,24,22]
youtube=[9,9,11,10,13,18,16]
tiktok=[19,21,18,23,27,32,29]
names=["Instagram","Youtube","Tiktok"]
data=[instagram,youtube,tiktok]
colors=["pink","red","black"]
fig,axes=plt.subplots(2,2,figsize=(12,8))
ax1=axes[0,0]
for i in range(3):
    ax1.plot(days,data[i],marker="o",label=names[i])
ax1.set_title("Daily Post trends")
ax1.set_xlabel("Days")
ax1.set_ylabel("Posts")
ax1.legend()
ax1.grid(True)

ax2=axes[0,1]
totals=[sum(values)for values in data]
ax2.bar(names,totals,color=colors)
ax2.set_title=("Total Weekly Posts")
ax2.set_xlabel("Platforms")
ax2.set_ylabel("Posts")

ax3=axes[1,0]
weekday=[sum(values[:5])/5 for values in data]
weekend=[sum(values[:5])/2 for values in data]
x=[0,1,2]
ax3.bar([i-0.2 for i in x],weekday,width=0.4,label="Weekday")
ax3.bar([i+0.2 for i in x],weekend,width=0.4,label="Weekend")
ax3.set_xticks(x)
ax3.set_xticklabels(names)
ax3.set_title("Weekday vs Weekend")
ax3.set_ylabel("Average posts")
ax3.legend()

ax4=axes[1,1]
ax4.fill_between(days,instagram,color="pink",alpha=0.5,label=instagram)
ax4.fill_between(days,tiktok,color="gray",alpha=0.5,label=tiktok)
ax4.plot(days,instagram,color="red")
ax4.plot(days,tiktok,color="black")
ax4.set_title("Instagram vs Tiktok")
ax4.set_title("Days")
ax4.set_ylabel("posts")
ax4.legend()
fig.suptitle("Social Media Trends Dashboard",fontsize=16)
plt.tight_layout()
plt.savefig("social_media_dashboard.png")
plt.show()