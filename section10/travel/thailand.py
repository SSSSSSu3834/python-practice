class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장투어) 50만원")

# 모듈 직접실행
# 모듈 안에서 실행할 때 실행됨
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 떄만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:  # 모듈 바깥에서 실행할 때 실행됨
    print("Thailand 외부에서 모듈 호출")