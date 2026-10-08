from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/linear-search', methods=['POST'])
def linear_search():
    """
    선형 검색 알고리즘을 수행하고 각 단계(Step)별 진행 상황을 반환하는 API입니다.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "요청 데이터(JSON)가 없습니다."}), 400
            
        array = data.get('array', [])
        target = data.get('target', None)
        
        # 유효성 검사
        if not isinstance(array, list) or target is None:
            return jsonify({"error": "'array'(리스트)와 'target'(검색할 값)을 정확히 전달해주세요."}), 400

        steps = []
        found_index = -1
        
        # 선형 검색 알고리즘 수행 (O(N))
        for index, element in enumerate(array):
            is_match = (element == target)
            
            # 각 비교 단계 기록
            steps.append({
                "step": index + 1,
                "current_index": index,
                "current_value": element,
                "target": target,
                "is_match": is_match,
                "description": f"인덱스 {index}의 값 {element}와(과) 목표값 {target}을(를) 비교합니다."
            })
            
            if is_match:
                found_index = index
                break  # 목표값을 찾으면 종료

        # 최종 응답 데이터 구성
        response = {
            "success": True,
            "target": target,
            "found_index": found_index,
            "total_steps": len(steps),
            "complexity": {
                "time_best": "O(1)",
                "time_worst": "O(N)",
                "time_average": "O(N)",
                "space": "O(1)"
            },
            "steps": steps
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Cloud Run 환경 변수에 맞춰 포트 지정
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
