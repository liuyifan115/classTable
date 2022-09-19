<template>
	<view class="content">
		<view class="input">
			<input placeholder="团队名称" v-model="teamname"/>
		</view>
		<view class="button">
			<button @click="creatteam">创建</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				teamname: '',
				teamid: uni.getStorageSync('teamid'),
			}
		},
		methods: {
			creatteam() {
				let that=this
				uni.request({
						url: 'http://127.0.0.1:8000/lesson/creatteam',
						method: 'POST',
						data: {
							teamname: this.teamname,
							username: uni.getStorageSync('username')
						},
						
						
					success: (res) => {
						if(res.data.status_code=='-114514'){
							uni.showToast({
								icon:'error',
								title:'团队名称已存在！',
							})
						}
						else if(res.data.status_code =='-1'){
							
							uni.showToast({
								icon:'error',
								title:'你已经在团队了',
							})
							uni.switchTab({
								url:'../main/main'
							})
						}
						else{
							uni.showToast({
								title:'创建成功',
							})
							uni.setStorageSync('teamid', res.data.teamid)
							uni.switchTab({
								url: '../creat/creat'
							})
						}
						}

					})
				},
		}
	}
</script>

<style>
.content{
	display: flex;
	flex-direction: column;
}
	
.input{
	display: flex;
	align-self: center;
	justify-self: center;
	align-content: center;
	justify-content: center;
	margin: 20rpx;
	width: 500rpx;
	background-color: whitesmoke;
	padding: 15rpx;
	border-radius: 30rpx;
}

.button{
	align-self: center;
	margin: 20rpx;
	border-radius: 30rpx;
	height: 50rpx;
	width: 200rpx;
}
</style>
